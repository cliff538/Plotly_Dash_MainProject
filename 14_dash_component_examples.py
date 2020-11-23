import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash

# Examples of RadioItems, Dropdowns, Slider
app = dash.Dash()

app.layout = html.Div([
    html.Label('City'),
    dcc.Dropdown(options=[{'label': 'New York City',
                           'value': 'NYC'},
                          {'label': 'San Francisco',
                           'value': 'SFO'}],
                 value='SFO'),
    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i: i for i in range(-10, 11)}),
    html.Label('Some Example Radio Items'),
    dcc.RadioItems(options=[{'label': 'New York City',
                             'value': 'NYC'},
                            {'label': 'San Francisco',
                             'value': 'SFO'}],
                   value='SFO')

])

if __name__ == '__main__':
    app.run_server()
