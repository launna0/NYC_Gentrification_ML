import pandas as pd
import altair as alt
import sankey as sk
import geopandas as gpd
from last_map import clean_areacode


alt.renderers.enable('altair_viewer')

# extracting root password from txt file
with open('password.txt') as infile:
    root_password = infile.readline().strip()


def construct_git():
    '''
    This function takes in a topojson through a raw git, and merges it with datasets with NTA codes and the clusters
    :return: a geojson with merged data to be converted externally
    '''
    nyc = "https://cdn.jsdelivr.net/gh/grantpezeshki/NYC-topojson@8ec416f320e5b0a4bd115699d3132148a2b35116/NTA.topojson"

    # read in NTA code csv, and clean the data
    areacode = clean_areacode()

    # read in clusters csv
    clusters = pd.read_csv('demographic_clusters.csv')
    clusters = clusters.drop('Unnamed: 0', axis=1)

    # call in SQL dump files and convert to pandas dataframe, extracting only rows with 2019
    demographics = sk.sql_to_df('gentrification', 'neighborhoodDemographics',
                                ['neighborhood', 'year', 'median_household_inc', 'white_prop*100', 'asian_prop*100',
                                 'black_prop*100', 'hispanic_prop*100', 'poverty_prop*100'], root_password,
                                column_headers=['neighborhood', 'year', 'median_household_income', 'white_percentage',
                                                'asian_percentage', 'black_percentage', 'hispanic_percentage',
                                                'poverty_rate'])
    demographics['neighborhood'] = demographics['neighborhood'].str.lower()
    demographics = demographics[demographics['year']==2019]

    # merge clusters and converted SQL datasets on neighborhood
    clusters = pd.merge(clusters, demographics, how='outer', on='neighborhood')

    # merge dataframe based on substrings found in the NTA dataframe, as names are longer
    str_match = "({})".format("|".join(clusters.neighborhood))

    merged = areacode.merge(clusters, left_on=areacode.neighborhood.str.extract(str_match)[0], right_on="neighborhood")

    # read in the topojson and convert to a geopandas dataframe
    # merge with the larger dataframe on NTA codes
    nyc_df = gpd.read_file(nyc)
    gdf = gpd.GeoDataFrame.from_features(nyc_df)
    gdf = gdf.merge(merged, on='NTACode', how='outer')

    # replace NAN values with string 'not enough data'
    gdf = gdf.fillna('not enough data')
    gdf = gdf.round(2)

    # replace cluster numbers with gentrification status
    map = {0: "Gentrifying", 1: 'Gentrified', 2: 'Not Gentrified', 'not enough data': 'not enough data'}
    gdf = gdf.apply(lambda row: sk.label_status(row, map), axis=1)
    gdf.to_file("cleaned.json", driver="GeoJSON")


def clustered_map(git):
    '''

    :param git: takes in a raw git link associated with a topojson
    :return: a constructed altair map with colors associated with clusters
    '''

    nyc_map = alt.topo_feature(git, feature="cleaned")

    # create altair map, with hover feature for name of the neighborhood and the associated demographic properties
    # set color to be equal to the gentrification status
    clustered_map = alt.Chart(nyc_map).mark_geoshape(stroke="black"
                                                     ).encode(
        tooltip=[alt.Tooltip("properties.name:N", title='name'), alt.Tooltip('properties.median_household_income:N',
                                                                             title='median household income'),
                 alt.Tooltip('properties.white_percentage:N', title='white proportion'),
                 alt.Tooltip('properties.black_percentage:N',
                             title=' black proportion'),
                 alt.Tooltip('properties.hispanic_percentage:N', title='hispanic proportion'),
                 alt.Tooltip('properties.asian_percentage:N',
                             title='asian proportion'),
                 alt.Tooltip('properties.poverty_rate:N', title='poverty rate')],
        color=alt.Color('properties.labels:N', title='gentrification status')).properties(
        width=700,
        height=700, title='NYC Neighborhoods Map'
    )

    return clustered_map


def uncolored_map(git):
    '''

    :param git: takes in a raw git link associated with a topojson
    :return: constructed altair map featuring the nyc neighborhoods
    '''

    nyc_map = alt.topo_feature(git, feature="collection")

    # construct altair map with hover feature that displays name of the neighborhood
    uncolored_map = alt.Chart(nyc_map).mark_geoshape(fill="lightgray", stroke="black"
                                                     ).encode(
        tooltip="properties.name:N").properties(
        width=700,
        height=700,
        title='NYC Neighborhoods Map'
    )
    return uncolored_map


if __name__ == "__main__":
    construct_git()
