import sankey as sk
import pandas as pd
from statistics import mean


def normalize_row(row, to_normalize):
    """

    :param row: series
        row of a df to have several elements be normalized by population
    :param to_normalize: list
        list of all columns to be normalized
    :return: series
        normalized row
    """
    for col in to_normalize:
        # normalize by every 100 residents in a given neighborhood
        row[col] = row[col] / (row["Population"] / 100)
    return row


def normalize_data(table, pop_nta_csv, nta_neigh_csv, database, selects, to_normalize, root_password, agg_funct,
                   year=None):
    """

    :param table: string
        either a csv for complaint data or the name of a table in an sql db
    :param pop_nta_csv: string
        the csv with population and nta codes
    :param nta_neigh_csv: string
        the csv with nta codes and neighborhoods
    :param database: string
        the database from which to pull data
    :param selects: list
        list of columns to get from the input table in the input db
    :param to_normalize: list
        list of columns to normalize by population
    :param root_password: string
        the user's root sql password
    :param agg_funct: string or function
        the aggregate function to group the input table on neighborhood with
    :param year: int
        the year to get normalized data for
    :return: dataframe
        df with normalized data
    """
    normalizer = get_population_data(pop_nta_csv, nta_neigh_csv)

    # get table_data based on if the input table is complaints or not. Complaint neighborhoods are in a csv, not in the
    # database, so there's a separate protocol for getting that data into a df
    if 'complaint' in table:
        table_data = pd.read_csv(table)
    else:
        table_data = sk.sql_to_df(database, table, selects, root_password)

    # if year is input as a parameter, get data only for that year and then possibly remove year from the df if it's
    # not being normalized
    if year:
        table_data = table_data[table_data['year'] == year]
        if 'year' not in to_normalize:
            table_data.drop(['year'], axis=1, inplace=True)
    # must convert data to numbers if the agg funct is mean to avoid a datatype error
    if agg_funct == mean:
        table_data[to_normalize] = table_data[to_normalize].apply(pd.to_numeric)

    table_data = table_data.groupby(['neighborhood'], as_index=False).agg({col: agg_funct for col in to_normalize})
    table_data['neighborhood'] = table_data['neighborhood'].str.lower()
    full_data = pd.merge(table_data, normalizer, on='neighborhood')

    # normalize the data
    normal_data = full_data.apply(lambda row: normalize_row(row, to_normalize), axis=1)

    if agg_funct == 'size':
        normal_data[to_normalize] = normal_data[to_normalize] * 100

    return normal_data


def get_population_data(pop_nta_csv, nta_neigh_csv):
    """

    :param pop_nta_csv: string
        the csv with population and nta codes
    :param nta_neigh_csv: string
        the csv with nta codes and neighborhoods
    :return: dataframe
        df with population and neighborhood data
    """
    pop_nta = pd.read_csv(pop_nta_csv)
    nta_neigh = pd.read_csv(nta_neigh_csv)
    nta_neigh.columns = ['borough', 'county', 'borough_code', 'puma', 'nta', 'NTA Code', 'neighborhood', 'last']
    pop_neigh = pd.merge(pop_nta, nta_neigh, on='NTA Code')
    pop_neigh = pop_neigh[['neighborhood', 'Population']]
    pop_neigh['Population'] = pop_neigh['Population'].str.replace('[^\w\s]', '')
    pop_neigh['Population'] = pop_neigh['Population'].apply(pd.to_numeric)
    pop_neigh['neighborhood'] = pop_neigh['neighborhood'].str.lower()
    return pop_neigh
