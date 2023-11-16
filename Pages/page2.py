import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.express as px
import pandas as pd
import numpy as np
import sankey as sk

# registering page 2 in the dashboard
dash.register_page(__name__)

# fetches root password from file
with open('password.txt') as infile:
    root_password = infile.readline().strip()

# reads data into dataframe and prepares for visualization
df = sk.sql_to_df('gentrification', 'neighborhoodDemographics',
               ['neighborhood', 'year', 'median_household_inc', 'white_prop*100', 'asian_prop*100', 'black_prop*100', 'hispanic_prop*100', 'poverty_prop*100'], root_password,
               column_headers=['neighborhood', 'year', 'median household income', 'white percentage', 'asian percentage', 'black percentage', 'hispanic percentage', 'poverty rate'])
# adds classification model results to dataframe
gent_status = pd.read_csv('demographic_clusters.csv', index_col=0)
df['neighborhood'] = df['neighborhood'].str.lower()
df = pd.merge(df, gent_status, how='inner', on='neighborhood')
map = {0: "Gentrifying", 1: 'Gentrified', 2: 'Not Gentrified'}
df = df.apply(lambda row: sk.label_status(row, map), axis=1)
df = df.rename(columns={'labels': 'gentrification status'})

# sets colors for nodes
color_map = {'median household income': (0, 100, 0), 'white percentage': (200, 0, 200), 'asian percentage': (200, 0, 200),
             'black percentage': (200, 0, 200), 'hispanic percentage': (200, 0, 200), 'poverty rate': (200, 0, 200),
             'gentrification status': (200, 0, 0)}


# call to make sankey and show visualization
sankey_fig = sk.make_sankey(df, ['median household income', 'white percentage'], ['white percentage', 'gentrification status'],
                            2019, 10, color_map=color_map)

# creates page layer
layout = html.Div([
        # all titles for all user input options
        dbc.Row(
            dbc.Col(
                # adding details and directions about visualisations
                html.P("The sankey diagram below plots the relationship between median household incomes, total population " 
                       "demographic percentage, and gentrification status of all classified neighborhoods."
                       " Control specifications within the sankey by selecting "
                       "between the 2010 and 2019 buttons, increasing or decreasing the number of value ranges, and the "
                       "choosing the center variable layer in the dropdown menu.",
                       style={'text-align': 'center', 'font-size': 16}),
                width={'size': 10, "offset": 1, 'order': 0}
            )
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown('Year Data is From'),
                        width={'size': 2, "offset": 1, 'order': 1}
                        ),
                dbc.Col(dcc.Markdown('Number of Value Ranges'),
                        width={'size': 2, "offset": 0, 'order': 2}
                        ),
                dbc.Col(dcc.Markdown('Center Variable Layer'),
                        width={'size': 2, "offset": 0, 'order': 3}
                        )
            ]
        ),
        # adds dash interactive components
        dbc.Row(
                [
                    dbc.Col(dcc.RadioItems([2010, 2019], 2019, inline=True, id='year'),
                            width={'size': 2, "offset": 1, 'order': 1}
                            ),
                    dbc.Col(dcc.Input(type='number', value=10, min=2, id='groups'),
                            width={'size': 2, "offset": 0, 'order': 2}
                            ),
                    dbc.Col(dcc.Dropdown(['white percentage', 'asian percentage', 'black percentage', 'hispanic percentage', 'poverty rate'],
                                         'white percentage', id='center_layer', placeholder="white percentage"),
                            width={'size': 2, "offset": 0, 'order': 3}
                            )
                ]
            ),
        # displays sankey graph
        dbc.Row(
            [
                dbc.Col(dcc.Graph(
                    id='graph',
                    figure=sankey_fig
                    )
                )

            ]
        )
], style={'border':'30px white solid'})


@callback(
    Output("graph", "figure"),
    Input("year", "value"),
    Input("groups", "value"),
    Input("center_layer", "value")
)
def update_sankey(year, groups, center_layer):
    # updates sankey figure based on user inputs
    sankey_fig = sk.make_sankey(df, ['median household income', center_layer],
                                [center_layer, 'gentrification status'], year, groups, color_map=color_map)

    return sankey_fig


