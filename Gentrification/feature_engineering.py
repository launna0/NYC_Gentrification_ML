from itertools import count

import pandas as pd
import mysql.connector
from geopy import distance
from statistics import mean
from IPython.display import display
import regex as re
import sankey as sk

from numpy import size


def dist(row_1, row_2):
    """

    :param row_1: series
        row of a dataframe to have distance calculated for
    :param row_2: series
        row of a dataframe to have distance calculated from
    :return: series
        row of a dataframe with a new distance column
    """
    lat_1 = row_2['latitude']
    lat_2 = row_1['latitude']
    long_1 = row_2['longitude']
    long_2 = row_1['longitude']
    distan = distance.geodesic((lat_1, long_1), (lat_2, long_2)).km
    row_1['dist'] = distan
    return row_1


def min_dist_neigh(row_input, df):
    """

    :param row_input: series
        row of a dataframe
    :param df: dataframe
        contains latitude and longitude data to calculate distance for the input row
    :return: series
        row of a dataframe with the neighborhood with the associated closest distance
    """
    df = df[df['borough'] == row_input['borough']]
    df_with_dist = df.apply(lambda row: dist(row, row_input), axis=1)
    min_idx = df_with_dist[['dist']].idxmin()
    min_neigh = df_with_dist.loc[min_idx]['neighborhood']
    min_neigh = ''.join(filter(lambda x: not x.isdigit(), min_neigh))

    row_input['neighborhood'] = min_neigh
    return row_input


def find_neighborhood(df, neighbor_df):
    """

    :param df: dataframe
        contains data that needs to be associated with a neighborhood
    :param neighbor_df: dataframe
        contains neighborhood latitude and longitude data
    :return: dataframe
        original dataframe with neighborhood column added
    """
    df = df[df['borough'] != '']
    df = df.apply(lambda row: min_dist_neigh(row, neighbor_df), axis=1)
    return df


def change_over_time(df, change_cols, agg_funct, change_years):
    """

    :param df: dataframe
        contains data the features will be engineered from
    :param change_cols: list
        contains columns to find change over time for
    :param agg_funct: function
        used for grouping by neighborhood and year
    :param change_years: list
        contains first and last year to calculate change over time for
    :return: dataframe
        has original features and engineered features
    """
    if agg_funct != 'size':
        df_neighs = df.groupby(['neighborhood', 'year']).agg({change_col: agg_funct for change_col in change_cols})
        df_change = pd.DataFrame()
        for neigh, subdf in df_neighs.groupby(level=0):
            subdf = subdf.droplevel(0)
            double = subdf.reset_index()
            df_temp = pd.DataFrame()
            for col in change_cols:
                # if there is info for both years, calculate change over time. If not, set it to zero
                if all([len(double) == 2, len(double) == 2]):
                    start = double[col][0]
                    stop = double[col][1]
                    result = ((stop - start) / start) * 100
                    df_temp['change in ' + col] = [result]
                    df_temp[str(change_years[1]) + ' ' + col] = stop
                    df_temp['neighborhood'] = neigh
                else:
                    df_temp['change in ' + col] = [0]
                    df_temp[str(change_years[1]) + ' ' + col] = 0
                    df_temp['neighborhood'] = neigh
            # populate df with engineered features
            df_change = pd.concat([df_change, df_temp])
    else:
        df = df[df['year'].isin(change_years)]
        df_neighs = df.groupby(['neighborhood', 'year']).agg(
            {change_col: agg_funct for change_col in change_cols}).rename(columns={'offense_level': 'size'})
        df_change = pd.DataFrame()
        for neigh, subdf in df_neighs.groupby(level=0):
            subdf = subdf.droplevel(0)
            double = subdf.reset_index()
            df_temp = pd.DataFrame()
            # if there is info for both years, calculate change over time. If not, set it to zero
            if all([len(double) == 2, len(double) == 2]):
                start = double[agg_funct][0]
                stop = double[agg_funct][1]
                result = ((stop - start) / start) * 100
                df_temp['change in ' + agg_funct] = [result]
                df_temp['neighborhood'] = neigh
                df_temp[str(change_years[1]) + ' ' + change_cols[0] + ' ' + agg_funct] = stop
            else:
                df_temp['change in ' + agg_funct] = [0]
                df_temp['neighborhood'] = neigh
                df_temp[str(change_years[1]) + ' ' + change_cols[0] + ' ' + agg_funct] = 0
            # populate dataframe with engineered features
            df_change = pd.concat([df_change, df_temp])
    return df_change


def main():
    with open('../password.txt', 'r') as infile:
        password = infile.readline().strip()
    # read in and clean neighborhood data
    neighborhoods = sk.sql_to_df('gentrification', 'neighborhoods', ['neighborhood',
                                                                  'latitude',
                                                                  'longitude',
                                                                  'borough'], password)
    neighborhoods['neighborhood'] = neighborhoods['neighborhood'].str.lower()
    neighborhoods['borough'] = neighborhoods['borough'].str.lower()
    neighborhoods = neighborhoods[neighborhoods['latitude'] != 'undefined)']
    neighborhoods = neighborhoods[neighborhoods['longitude'] != 'undefined)']
    neighborhoods[['latitude', 'longitude']] = neighborhoods[['latitude', 'longitude']].apply(pd.to_numeric)

    # read in and clean complaint data
    complaints = sk.sql_to_df('gentrification', 'nypdComplaints2015_2017', ['year',
                                                                         'latitude',
                                                                         'longitude',
                                                                         'offense_level',
                                                                         'borough'], password)
    complaints['borough'] = complaints['borough'].str.lower()
    complaints = complaints.dropna()
    complaints[['latitude', 'longitude']] = complaints[['latitude', 'longitude']].apply(pd.to_numeric)
    complaints = complaints[complaints['borough'] != '']

    # add neighborhoods to complaint data and save as a csv
    #complaints = find_neighborhood(complaints, neighborhoods)
    #complaints.to_csv('neighborhood_complaints.csv')

    # read in and clean demographic data
    demographics = sk.sql_to_df('gentrification', 'NeighborhoodDemographics', ['neighborhood',
                                                                            'year',
                                                                            'diversity_index',
                                                                            'poverty_prop',
                                                                            'white_prop',
                                                                            'median_household_inc',
                                                                            'singleunitbuilding_price',
                                                                            'asian_prop',
                                                                            'black_prop',
                                                                            'hispanic_prop'], password)
    demographics['neighborhood'] = demographics['neighborhood'].str.lower()
    demographics[['diversity_index',
                  'poverty_prop',
                  'white_prop',
                  'median_household_inc',
                  'singleunitbuilding_price',
                  'asian_prop',
                  'black_prop',
                  'hispanic_prop']] = demographics[['diversity_index',
                                                    'poverty_prop',
                                                    'white_prop',
                                                    'median_household_inc',
                                                    'singleunitbuilding_price',
                                                    'asian_prop',
                                                    'black_prop',
                                                    'hispanic_prop']].apply(pd.to_numeric)

    # engineer change over time features for demographic data and then save as csv as ml data
    demographics_over_time = change_over_time(demographics, ['diversity_index',
                                                             'poverty_prop',
                                                             'white_prop',
                                                             'median_household_inc',
                                                             'singleunitbuilding_price',
                                                             'asian_prop',
                                                             'black_prop',
                                                             'hispanic_prop'],
                                              mean,
                                              [2010, 2019])
    #demographics_over_time.to_csv('demographic_ml.csv')


if __name__ == '__main__':
    main()
