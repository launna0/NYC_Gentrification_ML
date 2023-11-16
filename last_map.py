import json
import pandas as pd
import sankey as sk
import matplotlib.pyplot as plt
import pydeck as pdk
from urllib.request import urlopen
from shapely.geometry import shape
import matplotlib.colors as colors
import matplotlib.cm as cmx
from normalize import *

mapbox_api_token = 'pk.eyJ1IjoiZGVlZGVlOCIsImEiOiJjbDF3YWNkMDcycTh1M2Ztb2U5ajV2ajYxIn0.ZZ_Vp4vuI8nHOveFryYMyw'


def clean_areacode():
    '''
    takes in a csv containing NTA codes and cleans it
    :return: a cleaned dataframe
    '''
     # read in csv to dataframe
    areacode = pd.read_csv("nyc2010census_tabulation_equiv.csv")
    # clean dataframe and keep only specified information
    areacode.columns = ['borough', 'county', 'borough_code', 'puma', 'nta', 'NTACode', 'neighborhood', 'last']
    areacode = areacode.filter(['borough', 'NTACode', 'neighborhood'], axis=1)
    areacode['neighborhood'] = areacode['neighborhood'].str.lower()
    areacode['neighborhood'] = areacode['neighborhood'].str.replace('-', ' ')

    return areacode


def unnormalized_dataframe(root_password, col_choice):
    '''

    :param root_password: root_password to access the SQL database
    :param col_choice: the column of the dataframe to look at
    :return: cleaned and merged dataframe, along with the column name to be used as height of columns
    '''
    # read in and call necessary dataframes
    areacode = clean_areacode()
    clusters = pd.read_csv('demographic_clusters.csv')
    clusters = clusters.drop('Unnamed: 0', axis=1)

    # call in SQL dump files and convert to pandas dataframe
    demographics = sk.sql_to_df('gentrification', 'neighborhoodDemographics',
                                ['neighborhood', 'year', 'median_household_inc', 'white_prop*100', 'asian_prop*100',
                                 'black_prop*100', 'hispanic_prop*100', 'poverty_prop*100'], root_password,
                                column_headers=['neighborhood', 'year', 'median_household_income', 'white_percentage',
                                                'asian percentage', 'black_percentage', 'hispanic percentage',
                                                'poverty_rate'])


    demographics['neighborhood'] = demographics['neighborhood'].str.lower()

    # merge clusters and converted SQL datasets on neighborhood
    clusters = pd.merge(clusters, demographics, how='outer', on='neighborhood')

    # merge dataframe based on substrings found in the NTA dataframe, as names are longer
    str_match = "({})".format("|".join(clusters.neighborhood))

    merged = areacode.merge(clusters, left_on=areacode.neighborhood.str.extract(str_match)[0], right_on="neighborhood")

    return merged, col_choice

def normalized_dataframe(root_password, table, selects, to_normalize, year):
    '''

    :param root_password: root_password to access the SQL database
    :param table: table from SQL to call in
    :param selects: information from SQL to keep
    :param to_normalize: which information/column must be normalized
    :param year: year to focus on
    :return: cleaned and normalized dataframe, along with a specified variable
    '''

    areacode = clean_areacode()
    # normalize the data based on parameters
    normalized_df = normalize_data(table, 'populations.csv', 'nyc2010census_tabulation_equiv.csv',
                                           'gentrification',
                                           selects, to_normalize, root_password,
                                           'size', year)

    # merge data based on substrings
    str_match = "({})".format("|".join(normalized_df.neighborhood))

    merged = areacode.merge(normalized_df, left_on=areacode.neighborhood.str.extract(str_match)[0],
                            right_on="neighborhood")

    return merged, to_normalize[0]



def construct_graph(root_password, value, normalized, table=None, selects=None, to_normalize=None, year=None,
                    col_choice=None, el_scale =None):
    """
    function: construct_graph
    :param: value : string of corresponding dropdown option
    :param normalized: boolean
    :param kwargs: optional parameters for normalized_df and construct_git functions if needed
    :return: returns a deck object and the mapbox api key
    """
    # if it is a normalized graph, then call the normalized_df function
    if normalized:
        merged, to_merge = normalized_dataframe(root_password, table, selects, to_normalize, year)

    # if data does not need to be normalized, then call the unnormalized_df function
    else:
        merged, to_merge = unnormalized_dataframe(root_password, col_choice)

    # read in the topojson
    with urlopen(
            'https://cdn.jsdelivr.net/gh/grantpezeshki/NYC-topojson@8ec416f320e5b0a4bd115699d3132148a2b35116/NTA.geojson') as nyc_geo:
        state_geo = json.load(nyc_geo)

    # set features as the features of the json
    features = state_geo["features"]
    # calculate the centroids based on the latitude and longitude of all the points associated in an NTA code
    centroids = {}
    for feature in features:
        s = shape(feature["geometry"])
        centroids[feature['properties']['NTACode']] = s.centroid

    # add the centroid latitude and longitudes to a new column in the dataframe
    merged["nta_lat"] = 0
    merged["nta_lon"] = 0
    for index, row in merged.iterrows():
        if row["NTACode"] in centroids:
            merged.loc[index, 'nta_lat'] = centroids[row["NTACode"]].y
            merged.loc[index, 'nta_lon'] = centroids[row["NTACode"]].x

    # set the view to be the latitude and longitudes of the centroids
    view = pdk.data_utils.compute_view(merged[["nta_lon", "nta_lat"]])
    view.pitch = 75
    view.bearing = 60

    # set the colors to be the feature that is meant to be plotted
    plasma = cm = plt.get_cmap('plasma')
    cNorm = colors.Normalize(vmin=merged[to_merge].min(), vmax=merged[to_merge].max())
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=plasma)
    merged["color"] = merged.apply(lambda row: scalarMap.to_rgba(row[to_merge]), axis=1)

    # create the columns using the position of each centroid, and using the feature that is meant to be plotted
    # as the height. scale it based on the parameter el_scale
    column_layer = pdk.Layer(
        "ColumnLayer",
        data=merged,
        get_position=["nta_lon", "nta_lat"],
        get_elevation=to_merge,
        elevation_scale=el_scale,
        radius=400,
        pickable=True,
        get_fill_color="[color[0] * 255, color[1] * 255, color[2] * 255, color[3] * 255]",
        auto_highlight=True,
    )

    # set the title to be the correct dataframe column name for the hover option
    if to_merge == 'median_household_income':
        tooltip_string = ["<b>",value,": {median_household_income} in {neighborhood} </b> "]

    elif to_merge == 'white_percentage':
        tooltip_string = ["<b>", value, ": {white_percentage} in {neighborhood} </b> "]

    elif to_merge == 'black_percentage':
        tooltip_string = ["<b>", value, ": {black_percentage} in {neighborhood} </b> "]

    elif to_merge == 'poverty_rate':
        tooltip_string = ["<b>", value, ": {poverty_rate} in {neighborhood} </b> "]

    elif to_merge == 'license_id':
        tooltip_string = ["<b>", value, ": {license_id} in {neighborhood} </b> "]

    elif to_merge == 'tree_id':
        tooltip_string = ["<b>", value, ": {tree_id} in {neighborhood} </b> "]

    else:
        tooltip_string = ["<b>", value, ": {change in size} in {neighborhood} </b> "]

    tooltip_string= " ".join(tooltip_string)
    tooltip = {
        "html": tooltip_string,
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                  "z-index": "10000"},
    }

    # create a deck object using the columns, the initial map positioning, and the mapbox style to be shown
    r = pdk.Deck(
        column_layer,
        initial_view_state=view,
        map_style="mapbox://styles/mapbox/satellite-v9"
    )

    return r, tooltip, mapbox_api_token

if __name__ == "__main__":
    construct_git('password')
