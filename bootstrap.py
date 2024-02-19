import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
        dbc.NavItem(dbc.NavLink("About Us", href="/about")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
    ],
    brand="Your Logo Here",
    brand_href="/",
    color="primary",
    dark=True,
)

# Define the footer
footer = dbc.Container(
    dbc.Row(
        dbc.Col([
            html.P("© 2024 All Rights Reserved Fujairah Research Centre"),
            html.P("PHONE: +971 92222411"),
            html.P("E-MAIL: info@frc.ae"),
            html.P("Location: Sakamkam, Fujairah, UAE"),
            html.A("Visit our website", href="https://frc.ae", target="_blank"),
        ]),
        align="center"
    ),
    fluid=True,
    className="footer"
)

# Define the app layout
app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        navbar,
        dbc.Container(id='page-content', children=[]),
        footer
    ],
    fluid=True,
)

# Callback to update page content based on navigation
@app.callback(
    dash.Output('page-content', 'children'),
    [dash.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/about':
        return html.Div([
            html.H1('About Us'),
            html.P('Our mission: "To achieve a sustainable economy in Fujairah through cutting-edge innovative research for: Efficient, safe, and sustainable use of natural resources. Strengthening regional agriculture, sustainable fisheries."')
        ])
    elif pathname == '/contact':
        return html.Div([
            html.H1('Contact Us'),
            html.P('PHONE: +971 92222411'),
            html.P('E-MAIL: info@frc.ae'),
            html.P('Location: Sakamkam, Fujairah, UAE'),
        ])
    else:
        # Your code to integrate the Plotly dashboard goes here
        return html.Div([
            html.H1('Dashboard'),
            # Embed your Plotly dash components or figures here
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
