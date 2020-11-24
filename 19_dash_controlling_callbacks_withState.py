# What if we wanted to wait before displaying the page? What if we wanted time to enter a series of changes
# before submitting them? This is where dash.dependencies State comes in. Dash offers the ability to store saved
# changes, and send them back on command. Consider this very basic example of Input/Output with a callback:
# 11/24/2020

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize': 28}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize': 28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('number-in', 'value')]
)
def output(n_clicks, number):
    return f'{number} displayed after {n_clicks} clicks of Submit Button.'

if __name__ == '__main__':
    app.run_server()



