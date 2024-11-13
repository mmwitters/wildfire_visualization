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
    dcc.Graph(figure={}, id='controls-and-graph'),
    html.Br(),
    html.Br(),
    dcc.Slider(2018, 2020, 1, value=2019, marks={2018: '2018', 2019:'2019', 2020:'2020'}, id='year-slider'),
]

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='year-slider', component_property='value')
)
def update_graph(year_chosen):
    df_year = df[df['FIRE_YEAR'] == int(year_chosen)]
    figure=px.scatter_geo(data_frame=df_year,
                     lat=df_year['LATITUDE'],
                     lon=df_year['LONGITUDE'], 
                     size=df_year['FIRE_SIZE'],
                     color=df_year['FIRE_SIZE'],
                     color_continuous_scale='YlOrRd',
                     scope='usa').update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return figure

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


