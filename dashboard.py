import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from app import app
from pages import home, page1, page2, page3
from components import navbar

# Build an app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


server = app.server
app.config.suppress_callback_exceptions = True

# set and create the navigation bar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
# connects paths with corresponding page layouts
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/page3':
        return page3.layout
    else:
        return home.layout


if __name__ == "__main__":
    app.run_server(debug=True)
