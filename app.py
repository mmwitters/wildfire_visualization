# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('/Users/madelinewitters/wildfire_data/test_dataset.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.scatter_geo(data_frame=df,
                     lat=df['LATITUDE'],
                     lon=df['LONGITUDE'], 
                     size=df['FIRE_SIZE'],
                     color=df['FIRE_SIZE'],
                     color_continuous_scale='YlOrRd',
                     scope='usa'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)