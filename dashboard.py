import dash
import dash_core_components as dcc
from dash import dcc, html
import dash_html_components as html
import pandas as pd

# Assume the weather_forecast.csv and prediction.csv files are in the same directory
weather_df = pd.read_csv('weather_forecast.csv')
prediction_df = pd.read_csv('predict_forecast.csv')

# Convert 'timestamp' column to datetime type
weather_df['timestamp'] = pd.to_datetime(weather_df['timestamp'])
prediction_df['date'] = pd.to_datetime(prediction_df['date'])

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Weather Forecast and Prediction Dashboard'),

    # Bar graph for temperature
    html.H2(children='Temperature by City'),
    dcc.Graph(
        id='temperature-bar',
        figure={
            'data': [
                {'x': weather_df['city'], 'y': weather_df['temperature'], 'type': 'bar', 'name': 'Temperature'},
                {'x': prediction_df['city'], 'y': prediction_df['temperature'], 'type': 'bar', 'name': 'Predicted Temperature'}
            ],
            'layout': {
                'title': 'Temperature by City',
                'xaxis': {'title': 'City'},
                'yaxis': {'title': 'Temperature (°C)'}
            }
        }
    ),

    # Bar graph for humidity
    html.H2(children='Humidity by City'),
    dcc.Graph(
        id='humidity-bar',
        figure={
            'data': [
                {'x': weather_df['city'], 'y': weather_df['humidity'], 'type': 'bar', 'name': 'Humidity'},
                {'x': prediction_df['city'], 'y': prediction_df['humidity'], 'type': 'bar', 'name': 'Predicted Humidity'}
            ],
            'layout': {
                'title': 'Humidity by City',
                'xaxis': {'title': 'City'},
                'yaxis': {'title': 'Humidity (%)'}
            }
        }
    ),

    # Add more bar graphs for other information as needed
])

# Run the app in the notebook
app.run_server(debug=True)

