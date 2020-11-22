import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Hello Dash!', style={'textAlign':'center'}),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='example',
              figure={'data':
                      'layout'})
])

if __name__ == '__main__':
    app.run_server()
