import dash
from dash import dcc, html, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import altair as alt
from altair_map import uncolored_map, clustered_map
import pandas as pd

alt.renderers.enable('altair_viewer')

# registering page 1 in the dashboard
dash.register_page(__name__)

nyc = "https://cdn.jsdelivr.net/gh/grantpezeshki/NYC-topojson@8ec416f320e5b0a4bd115699d3132148a2b35116/NTA.topojson"
nyc_topo = 'https://cdn.jsdelivr.net/gh/wang-grace/topojson-geojson@73d97ef4df4ddf1bef5f0718285ce8caf7365430/cleaned.json'

# import stats table csv file as a df
df = pd.read_csv('./Gentrification/stats_table.csv')
df = df.round(2)

layout = html.Div([
    dbc.Row(
        dbc.Col(
            # adding details and directions about visualisations
            html.P("The summary statistics table below displays the percentages of each variable of interest, "
                   "classified into their respective gentrification status. Scroll to view the entirety of the "
                   "table with all the variables that were utilized in the k-means clustering algorithm for "
                   "gentrification classification purposes. The map below was created with Altair and displays the "
                   "neighborhoods of NYC classified into Gentrified, Gentrifying, Not Gentrified, and not enough data. "
                   "Hover over a specific neighborhood and see its name and more details. Select a map type (uncolored"
                   " or colored) to view the map as either classified or unclassified.",
                   style={'text-align': 'center', 'font-size': 16}), width={'size': 10, "offset": 1, 'order': 0})
    ),
    dbc.Row(
        # creating the summary statistics table
        html.Div([dash_table.DataTable(
            df.to_dict('records'),
            [{"name": i, "id": i} for i in df.columns],
            fixed_columns={'headers': True,'data': 1},
            style_table={'overflowX': 'auto', 'minWidth': '100%'},
            style_header={'backgroundColor': 'pink', 'fontColor': 'white', 'fontWeight': 'bold', 'fontSize': 11},
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Gentrification Status']
            ],
            style_data={'whiteSpace': 'normal', 'height': 'auto', 'border': '1px solid pink'}),
            html.Br()
        ])
    ),
    dbc.Row(
        [
            dbc.Col(
                # creating dropdown selecting between colored vs. uncolored map
                html.Div([
                    html.H3('Select Map Type:', style={'font-size': 18}),
                    dcc.RadioItems(['uncolored', 'colored'], 'colored', inline=False, id='maptype')
                ]),
                width={'size': 3, "offset": 0, 'order': 1}
            ),
            dbc.Col(
                # mapping the outputted colored or uncolored altair map
                html.Div([html.Iframe(id='nymap', srcDoc=None,
                                      style={'width': '900px', 'height': '800px'})],
                         ),
                width={'size': 3, "offset": 0, 'order': 1}

            )
        ]
    )
], style={'border': '30px white solid'})


@callback(
    Output(component_id='nymap', component_property='srcDoc'),
    Input(component_id='maptype', component_property='value'))
def make_map(test):
    # return either colored or uncolored map based on dropdown selection
    if test == 'colored':
        git = nyc_topo
        nycmap = clustered_map(git)

    else:
        git = nyc
        nycmap = uncolored_map(git)

    # converting map to html format
    html_altair = nycmap.to_html()

    return html_altair
