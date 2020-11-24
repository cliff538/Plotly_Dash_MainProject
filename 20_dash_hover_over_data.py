import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

app.layout = html.Div([
    html.Div(dcc.Graph(id='wheels-plot',
                       figure={'data': [go.Scatter(
                           x=df['color'],
                           y=df['wheels'],
                           dy=1,
                           mode='markers',
                           marker={'size': 15}
                       )],
                        'layout': go.Layout(
                            title='Test',
                            hovermode='closest'
                        )}), style={'width': '30%', 'float': 'left'}),
    html.Div(html.Pre(id='hover-data',
                      style={'paddingTop': 35}),
             style={'width': '30%'}),

])

# 'hoverData' does not need to be defined above, it's a core component of any dcc.Graph
# can change to 'clickData' below and will change behavior or 'selectedData' on graph you select point with box select
# or lasso select
@app.callback(Output('hover-data', 'children'),
              [Input('wheels-plot', 'selectedData')])
def callback_image(hoverData):
    my_json_data = json.dumps(hoverData, indent=2)
    return my_json_data




if __name__ == '__main__':
    app.run_server()
