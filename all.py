import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Assuming Dash and dash_bootstrap_components are already installed
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
        dbc.NavItem(dbc.NavLink("About Us", href="/about")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
    ],
    brand="Fujairah Research Centre",
    brand_href="https://www.frc.ae",
    # brand_logo="/Users/simon/Desktop/Builds/Dashboard/frclogo.png",
    color="primary",
    dark=True,
)

# Footer
footer = html.Footer(
    children=[
        dbc.Container([
            html.P("© 2024 All Rights Reserved Fujairah Research Centre"),
            html.P("PHONE: +971 92222411"),
            html.P("E-MAIL: info@frc.ae"),
            html.P("Location: Sakamkam, Fujairah, UAE"),
            html.A("Visit our website", href="https://frc.ae", target="_blank"),
        ], fluid=True),
    ],
    style={'backgroundColor': '#f8f9fa', 'padding': '1rem', 'position': 'fixed', 'left': 0, 'bottom': 0, 'width': '100%', 'text-align': 'center'}
)

# App layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
    footer
])

# Callback to render page content
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return html.Div([
            # html.H1('About Us'),
            html.P('Our mission: "To achieve a sustainable economy in Fujairah through cutting-edge innovative research for: Efficient, safe, and sustainable use of natural resources. Strengthening regional agriculture and sustainable fisheries."')
        ])
    elif pathname == '/contact':
        return html.Div([
            html.H1('Contact Us'),
            html.P('PHONE: +971 92222411'),
            html.P('E-MAIL: info@frc.ae'),
            html.P('Location: Sakamkam, Fujairah, UAE'),
        ])
    elif pathname == '/':

        # file_path = '/Users/simon/Desktop/Builds/Dashboard/final.csv'
        file_path = '/Users/simon/Desktop/Builds/Dashboard/final.csv'

        data = pd.read_csv(file_path)

        # Convert the 'Time' column to a datetime format
        data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S.%f', errors='ignore')

        # Prepare a subplot layout if comparing multiple parameters
        fig = make_subplots(rows=len(data.columns[1:4]), cols=1, shared_xaxes=True,
                            vertical_spacing=0.02, subplot_titles=[f'Time vs. {param}' for param in data.columns[1:]])

        # Custom color palette
        colors = px.colors.qualitative.Plotly

        # Iterate over each parameter to create a subplot for each
        for i, parameter in enumerate(data.columns[1:4], start=1):
            fig.add_trace(go.Scatter(x=data['Time'], y=data[parameter], mode='lines+markers',
                                    name=parameter, line=dict(color=colors[i % len(colors)], width=2),
                                    marker=dict(size=5, line=dict(width=1, color='DarkSlateGrey')),
                                    showlegend=True),
                        row=i, col=1)

        # Update layout for a cohesive look
        fig.update_layout(height=300*len(data.columns[1:]), width=1000, title_text=f"Camel {data.columns[6]}",
                        title_font_size=24, template='plotly_dark',
                        hovermode='x unified')

        fig.update_xaxes(showline=True, linewidth=2, linecolor='gray', mirror=True)
        fig.update_yaxes(showline=True, linewidth=2, linecolor='gray', mirror=True)

        # Improve hover information
        fig.update_traces(hovertemplate='Time: %{x}<br>Value: %{y}')

        # Show the plot
        # fig.show()

        return dcc.Graph(figure=fig)
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
