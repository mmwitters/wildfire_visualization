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
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['2018', '2019', '2020'], value='2018', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
]

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
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


