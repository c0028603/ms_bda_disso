import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv("/Users/raveendrababupasumarthi/Documents/Py/sh6/dataset.csv")

# Create Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Raveendra SH6 SuperHalfs(Half Marathon) Series Analysis Dashboard"),

    # Map Visualization
    dcc.Graph(
        id='map-plot',
        figure=px.scatter_geo(df, locations='Country', locationmode='country names', color='Duration in Min',
                              hover_name='City', size='Duration in Min', title='Geo Half Marathon Map by City')
                 #.update_layout(config={'displayModeBar': False, 'displaylogo': False})
                 .update_traces(hoverinfo='text')

          
    ),
  
    # Time Analysis Line Chart
    dcc.Graph(
        id='time-line-chart',
        figure=px.line(df, x='Date', y='Duration in Min', title='Run Time Analysis Over Timeline')
    ),

    # Pace Analysis Scatter Plot
    dcc.Graph(
        id='pace-scatter-plot',
        figure=px.scatter(df, x='Duration in Min', y='Pace', color='Country', title='Pace Analysis')
    ),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
