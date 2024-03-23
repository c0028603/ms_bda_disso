import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv("dataset.csv")

# Create Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Half Marathon Analysis Dashboard"),

    # Map Visualization
    dcc.Graph(
        id='map-plot',
        figure=px.scatter_geo(df, locations='Country', locationmode='country names', color='Duration',
                              hover_name='City', size='Duration', title='Half Marathon Map')
                 #.update_layout(config={'displayModeBar': False, 'displaylogo': False})
                 .update_traces(hoverinfo='text')

          
    ),
  
    # Time Analysis Line Chart
    dcc.Graph(
        id='time-line-chart',
        figure=px.line(df, x='Date', y='Duration', title='Time Analysis Over Dates')
    ),

    # Pace Analysis Scatter Plot
    dcc.Graph(
        id='pace-scatter-plot',
        figure=px.scatter(df, x='Duration', y='Pace', color='Country', title='Pace Analysis')
    ),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
