import pandas as pd
import sklearn
import numpy as np
from sklearn.cluster import KMeans
from statistics import mean
import seaborn as sns
import matplotlib.pyplot as plt


def k_means(k, df):
    """

    :param k: int
        the number of clusters to make
    :param df: dataframe
        contains the data to be clustered
    :return inertia: float
        the inertia for the k means model
    """
    df_no_neigh = df.drop(['neighborhood'], axis=1, inplace=False)
    X = df_no_neigh.to_numpy()
    model = KMeans(n_clusters=k, init='k-means++', random_state=42).fit(X)
    inertia = model.inertia_
    return inertia


def elbow_graph(data, k_vals):
    """

    :param data: dataframe
        contains data to find the correct number of clusters for
    :param k_vals: list
        contains the cluster numbers to check
    :return: None
    """
    inertias = []
    for k in k_vals:
        inertia = k_means(k, data)
        inertias.append(inertia)
    sns.lineplot(x=k_vals, y=inertias)
    plt.xlabel("K Value")
    plt.ylabel("Model Inertia")
    plt.title("K Values Verses Inertia for K-Means Clustering")
    plt.show()


def main():
    data = pd.read_csv('complaints_data.csv')
    data = data.fillna(0)
    data = data.groupby(['neighborhood'], as_index=False).agg(mean)
    k_vals = list(range(1, 10))

    elbow_graph(data, k_vals)


if __name__ == '__main__':
    main()
