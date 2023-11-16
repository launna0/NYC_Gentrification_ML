import pandas as pd
import sklearn
import numpy as np
from sklearn.cluster import KMeans
from statistics import mean


def k_means(k, df):
    """

    :param k: int
        the number of clusters to create
    :param df: dataframe
        contains the data to be clustered
    :return: dataframe
        contains clusters and their labels
    """
    df_no_neigh = df.drop(['neighborhood'], axis=1, inplace=False)
    X = df_no_neigh.to_numpy()
    model = KMeans(n_clusters=k).fit(X)

    # build and save as a csv a dataframe that contains neighborhoods and their cluster labels
    y = pd.DataFrame()
    y['labels'] = model.labels_
    y['neighborhood'] = df['neighborhood']
    y.to_csv('complaint_clusters_.csv')
    return y


def avg_label_data(cluster_data, overall_data):
    """

    :param cluster_data: dataframe
        contains clusters and their labels
    :param overall_data: dataframe
        contains the data the clusters were calculated from
    :return: None
    """
    compare = pd.merge(cluster_data, overall_data, on='neighborhood')

    # group the data by cluster label to get averages for each cluster. These will be used to identify cluster labels
    # as a gentrification status
    compare = compare.groupby(['labels']).agg(mean)
    compare.to_csv('compare_complaint.csv')


def main():
    data = pd.read_csv('complaints_data.csv')
    data = data.fillna(0)
    data = data.groupby(['neighborhood'], as_index=False).agg(mean)
    y = k_means(3, data)

    avg_label_data(y, data)


if __name__ == '__main__':
    main()
