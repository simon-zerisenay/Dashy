import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the CSV file

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
fig.show()
