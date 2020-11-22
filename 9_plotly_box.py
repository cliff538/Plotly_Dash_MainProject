import plotly.offline as pyo
import plotly.graph_objs as go

#y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]


# boxpoints='all' gives you all the data points(scatter plot) along side box summary. "outliers" gives you just max/min.
# jitter 0 to 1.0 gives offset on your scatter points. pointpos=0 gives you scatter on top of box, negative number to
# and positive number to right of box, range is -2 to 2.
#data = [go.Box(y=y, boxpoints='outliers', jitter=0, pointpos=0)]

data = [go.Box(y=snodgrass, name='Snodgrass', boxpoints='all', jitter=0.2, pointpos=1.5),
        go.Box(y=twain, name='Twain', boxpoints='all', jitter=0.2, pointpos=2)]


pyo.plot(data)

