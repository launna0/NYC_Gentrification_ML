import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import altair as alt
import sankey as sk

alt.renderers.enable('altair_viewer')
import json
import numpy as np
import geopandas as gpd


def construct_git():
    nyc = "https://cdn.jsdelivr.net/gh/grantpezeshki/NYC-topojson@8ec416f320e5b0a4bd115699d3132148a2b35116/NTA.topojson"

    areacode = pd.read_csv("nyc2010census_tabulation_equiv.csv")
    areacode.columns = ['borough', 'county', 'borough_code', 'puma', 'nta', 'NTACode', 'neighborhood', 'last']
    areacode = areacode.filter(['borough', 'NTACode', 'neighborhood'], axis=1)
    areacode['neighborhood'] = areacode['neighborhood'].str.lower()
    areacode['neighborhood'] = areacode['neighborhood'].str.replace('-', ' ')
    clusters = pd.read_csv('demographic_clusters.csv')
    clusters = clusters.drop('Unnamed: 0', axis=1)


    demographics = sk.sql_to_df('gentrification', 'neighborhoodDemographics',
                      ['neighborhood', 'year', 'median_household_inc', 'white_prop*100', 'asian_prop*100',
                       'black_prop*100', 'hispanic_prop*100', 'poverty_prop*100'], root_password,
                      column_headers=['neighborhood', 'year', 'median household income', 'white percentage',
                                      'asian percentage', 'black percentage', 'hispanic percentage', 'poverty rate'])
    demographics['neighborhood'] = demographics['neighborhood'].str.lower()

    clusters = pd.merge('clusters', 'demographics', how = 'outer', on ='neighborhood')

    str_match = "({})".format("|".join(clusters.neighborhood))

    merged = areacode.merge(clusters, left_on=areacode.neighborhood.str.extract(str_match)[0], right_on="neighborhood")

    nyc_df = gpd.read_file(nyc)
    gdf = gpd.GeoDataFrame.from_features(nyc_df)
    gdf = gdf.merge(merged, on='NTACode', how='outer')
    gdf['labels'] = gdf['labels'].fillna('not enough data')
    map = {0: "Gentrifying", 1: 'Gentrified', 2: 'Not Gentrified'}
    gdf = gdf.apply(lambda row: sk.label_status(row, map), axis=1)
    #gdf['labels'] = gdf['labels'].replace(0, 'gentrifying')
    #gdf['labels'] = gdf['labels'].replace(1, 'gentrified')
   # gdf['labels'] = gdf['labels'].replace(2, 'not gentrified')
    gdf.to_file("demographics_geo.json", driver="GeoJSON")

    #nyc_merge = 'https://cdn.jsdelivr.net/gh/wang-grace/topojson-geojson@ff2a2eb1108ae3262b873e30ee0404d7ee05a191/output_cluster.json'


def clustered_map(git):




    nyc_map = alt.topo_feature(git, feature="output_cluster")

    clustered_map = alt.Chart(nyc_map).mark_geoshape(stroke="black"
                                     ).encode(
        tooltip="properties.name:N", color=alt.Color('properties.labels:N', title='gentrification status')).properties(
        width=780,
        height=780,  title='NYC Neighborhoods Map'
    )

    return clustered_map





def uncolored_map(git):
    nyc_map = alt.topo_feature(git, feature="collection")

    uncolored_map = alt.Chart(nyc_map).mark_geoshape(fill="lightgray", stroke="black"
                                              ).encode(
        tooltip="properties.name:N").properties(
        width=780,
        height=780,
        title='NYC Neighborhoods Map'
    )
    return uncolored_map



if __name__ == "__main__":
    construct_git()