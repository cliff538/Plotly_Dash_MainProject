#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

'''
Because in mocksurvey.csv the questions (Question1, Question2, etc)
appear in the index you have to set them as index_col=0.

Horizontal Bar Chart: reverse x and y and add orientation='h'.

'''

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go



# create a DataFrame from the .csv file:
df = pd.read_csv('data/mocksurvey.csv', index_col=0)
print(df)

# create traces using a list comprehension:
data = [go.Bar(x=df[i],
               y=df.index,
               orientation='h',
               name=i)
               for i in df.columns]

print(data)


layout = go.Layout(title='Survey Results', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='survey_results_horizontal.html')