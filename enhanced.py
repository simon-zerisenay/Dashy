import pandas as pd
import plotly.express as px

# Assuming 'file_path' is the path to your CSV file
file_path = '/Users/simon/Desktop/Builds/Dashboard/final.csv'
data = pd.read_csv(file_path)

# Convert the 'Time' column to a datetime format if it's not already
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S.%f', errors='ignore')

# Iterate over each parameter except for 'Time' to plot them
for parameter in data.columns[1:]:  # Skip the first column assuming it's 'Time'
    fig = px.line(data, x='Time', y=parameter, title=f'Time vs. {parameter}',
                  labels={'Time': 'Time', parameter: parameter},
                  template='plotly_white')  # Use a clean template

    # Improve the design
    fig.update_layout(
        title={'text': f'Time vs. {parameter}', 'font': {'size': 24}, 'x': 0.5, 'xanchor': 'center'},
        plot_bgcolor='white',  # Set plot background to white for a cleaner look
        xaxis_title='Time',
        yaxis_title=parameter,
        legend_title='Legend',
        font=dict(family="Arial, sans-serif", size=18, color="RebeccaPurple")
    )

    # Customize line and marker
    fig.update_traces(line=dict(width=3), marker=dict(size=7))

    # Customize hover information
    # fig.update_traces(hoverinfo="all", hovertemplate=f'Time: %{x}<br>{parameter}: %{y}')
    # Customize hover information
    fig.update_traces(hoverinfo="all", hovertemplate=f'Time: %{{x}}<br>{parameter}: %{{y}}')


    # Show the plot
    fig.show()
