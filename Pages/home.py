import dash
from dash import html
import base64

# registering home page in the dashboard
dash.register_page(__name__)

# fetches storefront image
image_filename = 'storefront.png'

def b64_image(image_filename):
    # decodes the storefront image
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

# creates page layer
layout = html.Div([
    html.Div(
        children=html.Div([
            # Header that displays project title
            html.H1('NYC Gentrification', style={'text-align': 'center', 'font-size': '40px'}),
            # Smaller header display project authors
            html.H3("Authors: Launna Atkinson, Christina He, Claudia Levi, Nidhi Pillai, Grace Wang",
                    style={'text-align': 'center', 'font-size': '24px'}),
            # Add project premise and details about visualisation components included in each page
            html.Div([
                html.P("Gentrification is a prominent global issue that affects an area’s history and culture and "
                       "reduces social capital. While gentrification often increases the economic value of a neighborhood, "
                       "it also leads to many negative impacts, such as forced displacement of low-income families, "
                       "discriminatory behavior by people in power, and unequal residential outcomes for poor residents "
                       "by race. Our goal for the project was to visualize the effects of gentrification over time on "
                       "different neighborhoods in NYC and how it affects different demographic populations. We analyzed "
                       "various variables of interest, such as the diversity index, poverty rate, household income, and "
                       "racial demographics, through 2010-2019 and used a k-means unsupervised clustering algorithm to "
                       "classify each neighborhood into their respective gentrification status. Our classification model "
                       "was able to classify over 100 NYC neighborhoods into gentrified, gentrifying, and not gentrified "
                       "classifications.", style={'text-align': 'center', 'font-size': '20px'}),
                html.P("The dashboard consists of Home page introducing the premise of the project, a Gentrification Map "
                       "tab consisting of an altair map of NYC boroughs, a Sankey tab with an interactive sankey diagram, "
                       "and a 3D Map tab of a pydeck 3-dimensional column layer map of all the NYC neighborhoods. As "
                       "a result, we found that gentrification marginalizes minority populations and increases "
                       "inequalities between neighborhoods. Monitoring these trends allows us to predict where "
                       "gentrification may be occurring and possibly implement policies or programs that can combat the "
                       "negative effects.",
                       style={'text-align': 'center', 'font-size': '20px'})
            ], style={'border':'40px white solid'}),
            # Adds the storefront image into the home page
            html.Div([
                html.Img(src=b64_image(image_filename), style={'height': '300px', 'width': '510px'}),
                ], style={'textAlign': 'center'}
            ),
        ], style={'border':'40px white solid'}),
    ),
])
