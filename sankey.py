import mysql.connector
import pandas as pd
import numpy as np
from collections import defaultdict
import plotly.graph_objects as go
from plotly.graph_objects import Layout
from pandas.api.types import is_numeric_dtype


def _get_tint(rgb_orig, tint_ind, tint_tot):
    """

    :param rgb_orig: tuple, an rgb value
    :param tint_ind: int, higher number corresponds to lighter tint (maximum value is tint_tot)
    :param tint_tot: int, total number of tints that will be made for rgb
    :return: rgb_tint: string, 'rgb(x, x, x)' that represents a tint of rgb_orig
    """
    rgb_tint = []
    for val in rgb_orig:
        rgb_tint.append(val + ((255 - val) * (tint_ind / tint_tot)))
    return 'rgb' + str(tuple(rgb_tint))

def _code_mapping(df, groups, color_map=None, *vars):
    """Maps labels/strings in source and target
    and converts them to integers 0,1,2,3..."""

    # Converts vars (src(s) and targ(s)) into a list
    vars = list(vars)
    df = df.dropna(subset=vars)

    # Generates color map if not given
    if color_map is None:
        color_map = dict(zip(vars, [tuple(np.random.choice(range(256), size=3)) for var in vars]))

    # Separates variables by type
    vars_num = [var for var in vars if is_numeric_dtype(df[var])]
    vars_str = [var for var in vars if var not in vars_num]

    # Extract labels for numeric variables
    # vals = [{'income': [list of income vals]}, {'white prop': [list]}, {'gent_status': []}]
    # list of dicts

    vals = [{var: sorted(list(df[var]))} for var in vars_num]

    # Defines range constraints for groups of each variable
    range_size = [int((df[var].max()-df[var].min())//(groups-1)) for var in vars_num]
    range_vals = [sorted(list(range(int(df[var].min()), int(df[var].max() + ((df[var].max()-df[var].min())//(groups-1))),
                                    int((df[var].max()-df[var].min())//(groups-1))))) for var in vars_num]

    # Pair variable values with code
    lc_map = []
    start_ind = 0
    for i in range(len(vals)):
        curr_map = defaultdict(dict)
        # iterates over all values of a variable
        for j in range(len(vals[i][vars_num[i]])):
            # Determines which range the value lies within and adds code to map
            range_vals[i].append(vals[i][vars_num[i]][j])
            range_vals[i].sort()
            if len(range_vals[i]) == len(set(range_vals[i])):
                curr_map[vals[i][vars_num[i]][j]] = range_vals[i].index(vals[i][vars_num[i]][j]) - 1 + start_ind
            else:
                curr_map[vals[i][vars_num[i]][j]] = range_vals[i].index(vals[i][vars_num[i]][j]) + start_ind
            range_vals[i].remove(vals[i][vars_num[i]][j])

        # updates first index value for next variable
        start_ind += len(range_vals[i])
        lc_map.append(curr_map)


    # In df, substitute codes for labels
    for i in range(len(vars_num)):
        df = df.replace({vars_num[i]: lc_map[i]})

    # Generates string labels for each group of values
    labels = [str(int(range_vals[i][j])) + '-' + str(int(range_vals[i][j])+range_size[i])
              for i in range(len(range_vals)) for j in range(len(range_vals[i]))]

    # Generates rgb colors for each group of values
    colors = [_get_tint(color_map[vars_num[i]], j, groups-1)
              for i in range(len(range_vals)) for j in range(len(range_vals[i]))]


    # Extract distinct labels and colors for string variables
    labels_str = [{var: list(set(list(df[var])))} for var in vars_str]
    colors_str = [_get_tint(color_map[key], i, len(subdict[key])-1) for subdict in labels_str for key in subdict.keys() for i in range(len(subdict[key]))]
    labels_str = list(set([val for subdict in labels_str for value in subdict.values() for val in value]))

    # Define integer codes for string variables
    codes_str = range(start_ind, start_ind + len(labels_str))

    # Pair labels with list
    lc_map_str = dict(zip(labels_str, codes_str))

    # In df, substitute codes for labels
    for var in vars_str:
        df = df.replace({var: lc_map_str})

    # combines labels and colors lists for numeric and string variables
    labels = labels + labels_str
    colors = colors + colors_str

    return df, labels, colors

def _make_df(df, src, targ, year, min_threshold=0, src_domain=None):
    """Creates dataframe that has source, target, and value columns"""

    # gets data only from specified year
    df = df.loc[df['year'] == year]

    # groups data by src and targ, and counts frequency
    df_grouped = df.groupby([src, targ], as_index=False).size()

    # removes rows whose count are below the minimum threshold
    df_grouped = df_grouped[df_grouped['size'] > min_threshold]

    if src_domain:
        df_grouped = df_grouped[df_grouped[src].isin(src_domain)]

    return df_grouped

def sql_to_df(database, table, selects, root_password, **kwargs):
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user='root',
                                         password=root_password)
    sql_select_query = "select " + ' ,'.join(selects) + " from " + table
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    column_headers = kwargs.get('column_headers', selects)
    df = pd.DataFrame(cursor.fetchall(), columns=column_headers)
    return df

def make_sankey(df, src, targ, year, groups=None, color_map=None, **kwargs):
    """Generates the sankey diagram"""

    # code maps all attribute values
    vars = list(set(src + targ))
    df, labels, colors = _code_mapping(df, groups, color_map, *vars)

    # creates df with all sources, targets, and values
    df_link = pd.DataFrame(columns=['source', 'target', 'size'])
    for i in range(len(src)):
        if i > 0:
            df_temp = _make_df(df, src[i], targ[i], year, kwargs.get('min_threshold', 0), src_domain=targ_domain)
        else:
            df_temp = _make_df(df, src[i], targ[i], year, kwargs.get('min_threshold', 0))

        # adds current level link to df
        df_temp.rename(columns={src[i]: 'source', targ[i]: 'target'}, inplace=True)
        df_link = pd.concat([df_link, df_temp])

        # stores previous level's target domain, so next level's source domain is the same
        targ_domain = list(df_temp.target.unique())

    # sets parameters for sankey diagram and creates diagram
    pad = kwargs.get('pad', 50)
    thickness = kwargs.get('thickness', 30)
    line_color = kwargs.get('line_color', 'black')

    link = {'source': df_link['source'], 'target': df_link['target'], 'value': df_link['size']}
    node = {'label': labels, 'pad': pad, 'thickness': thickness, 'line_color': line_color, 'color': colors}

    sk = go.Sankey(link=link, node=node)

    # makes grid not visible
    layout = Layout(plot_bgcolor='rgba(0,0,0,0)')
    fig = go.Figure(sk, layout=layout)

    # labels layers
    layers = src + [elem for elem in targ if elem not in src]
    for x_coor, layer_name in enumerate(layers):
        fig.add_annotation(
            x=x_coor,
            y=1.075,
            xref="x",
            yref="paper",
            text=layer_name.title(),
            showarrow=False,
            # font=dict(
            #     family="Tahoma",
            #     size=16,
            #     color="black"
            # ),
            align="left",
        )

    # removes x and y axes
    fig.update_xaxes(showgrid=False, color='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=False, color='rgba(0,0,0,0)')

    return fig

def label_status(row, map):
    """Labels gentrification status"""
    row['labels'] = map[row['labels']]
    return row
