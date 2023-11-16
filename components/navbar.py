# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():
    # Creates the nagivation bar that contains the different page of visualizations
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                # Title the page name and link
                dbc.NavItem(dbc.NavLink("Gentrification Map", href="/page1")),
                dbc.NavItem(dbc.NavLink("Sankey", href="/page2")),
                dbc.NavItem(dbc.NavLink("3D Map", href="/page3")),
            ] ,
            # Title navbar
            brand="Group 12: DS3500 Final Project",
            # Have the intial page of dashboard begin on the home page
            brand_href="/home",
            color="dark",
            dark=True,
        ),
    ])

    return layout
