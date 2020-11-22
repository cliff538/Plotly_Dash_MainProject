import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


# get some random data.
np.random.seed(56)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)
print(x_values)
print(y_values)

# y=y_values+5(-5) is to seperate the traces on the chart for reference
trace0 = go.Scatter(x=x_values,y=y_values+5,
                   mode='markers',name='markers')

trace1 = go.Scatter(x=x_values,y=y_values,
                    mode='lines',name='mylines')

trace2 = go.Scatter(x=x_values,y=y_values-5,
                    mode='lines+markers',name='info baby')

data = [trace0, trace1, trace2]

# layout sets chart title and x,y labels, etc.
layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data,layout=layout)

# actually makes the chart
pyo.plot(fig,filename='line.html')

