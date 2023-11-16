from last_map import *
import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_deck

# registering page 3 in the dashboard
dash.register_page(__name__)

# extracting root password from txt file
with open('password.txt') as infile:
    root_password = infile.readline().strip()

# fetches the columns, tooltip, and map image from last_map
r, tooltip, api_keys = construct_graph(root_password, value='median household income', normalized=False,
                                       col_choice='median_household_income')

# creates the card that the map will be displayed in
card = dbc.Card(
    dbc.CardBody([html.Div(
        dash_deck.DeckGL(
            r.to_json(), id="deck-gl", tooltip=tooltip, mapboxKey=api_keys
        ),
        style={"height": "550px", "width": "100%", "position": "relative"},
    )]))

# setting deck container variable as a separate html section with the plotted map
deck_container = html.Div(
    dash_deck.DeckGL(
        r.to_json(), id="deck-gl", tooltip=tooltip, mapboxKey=api_keys
    ),
    style={"height": "550px", "width": "100%", "position": "relative"},
)

# creates page layer
layout = html.Div([
    html.Div([dbc.Row(
        [
            dbc.Col(
                html.H3('Select the viewed variable:', style={'font-size': 18}),
                width={'size': 2, "offset": 0, 'order': 1}),
            dbc.Col(
                html.H3("Zoom in to view the map!", style={'text-align': 'center', 'font-size': 38}),
                width={'size': 6, "offset": 1, 'order': 2})
        ]
    ),
        dbc.Row(
            [
                dbc.Col(
                    # creating dropdown selection for the specified variable
                    dcc.Dropdown(['median household income', 'poverty rate', 'white proportion', 'black proportion',
                                  'proportion of businesses per 10,000 people',
                                  'proportion of trees per 10,000 people',
                                  'proportion of crime reports count per 10,000 people'],
                                 'median household income', id='maptype'),

                    width={'size': 3, "offset": 0, 'order': 1}),
                dbc.Col(
                    html.P("The 3D map below was constructed with pydeck's ColumnLayer visualization, which includes "
                           "normalized data of different variables of interest. "
                           "Zoom in on the map to display the satellite map background and control the "
                           "columns displayed by selecting a variable in the dropdown menu. Hover of each column to "
                           "view details about the variable of interest for each neighborhood in NYC.",
                           style={'text-align': 'center', 'font-size': 16}),
                    width={'size': 7, "offset": 0, 'order': 2})
            ]),
    ]),

    # displaying map with variable heights
    html.Div([
        dbc.Row(id='card', children=card)
    ])
], style={'border': '30px white solid'})


@callback(
    Output('card', 'children'),
    Input('maptype', 'value')
)
def update_3d_map(variable):
    # connects the user-selected variable from the dropdown menu with the map columns
    if variable == 'white proportion':
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=False,
                                               col_choice='white_percentage', el_scale =400)

    elif variable == 'median household income':
        r, tooltip, api_keys = construct_graph(root_password, value='median household income', normalized=False,
                                               col_choice='median_household_income', el_scale =.15)

    elif variable == 'poverty rate':
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=False,
                                               col_choice='poverty_rate', el_scale = 1000)

    elif variable == 'black proportion':
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=False,
                                               col_choice='black_percentage', el_scale =500)

    elif variable == 'proportion of businesses per 10,000 people':
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=True,
                                               table='businesses', selects=['license_id', 'year', 'neighborhood'],
                                               to_normalize=['license_id'],
                                               year=2020, el_scale= 3000)
    elif variable == 'proportion of trees per 10,000 people':
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=True,
                                               table='trees', selects=['tree_id', 'neighborhood'],
                                               to_normalize=['tree_id'], el_scale = 5
                                               )
    else:
        r, tooltip, api_keys = construct_graph(root_password, value=variable, normalized=True,
                                               table='complaints_data.csv', selects=['change in size', 'neighborhood'],
                                               to_normalize=['change in size'], el_scale = 100000
                                               )
    # creates the contents of the card and includes all map features together
    card = dbc.Card(
        dbc.CardBody([html.Div(
            dash_deck.DeckGL(
                r.to_json(), id="deck-gl", tooltip=tooltip, mapboxKey=api_keys
            ),
            style={"height": "550px", "width": "100%", "position": "relative"},
        )]))

    return card
