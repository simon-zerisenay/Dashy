import pandas as pd
import plotly.express as px

# Load the CSV file
# file_path = '/path/to/your/csv/file.csv'  # Make sure to update this path to your actual file location
file_path = '/Users/simon/Desktop/Builds/Dashboard/race_20240103_042233.csv'
data = pd.read_csv(file_path) 

# Assuming the first column is 'Time' and it's in a recognizable format, convert it to datetime
data['Time'] = pd.to_datetime(data.iloc[:, 0], format='%H:%M:%S.%f', errors='ignore')

# Iterate over all columns except the first one ('Time')
for parameter in data.columns[1:]:
    # Creating the plot for each parameter against 'Time'
    fig = px.line(data, x='Time', y=parameter, title=f'Time vs. {parameter}')
    
    # Showing the plot
    fig.show()
