#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

'''
Because in mocksurvey.csv the questions (Question1, Question2, etc)
appear in the index you have to set them as index_col=0.

'''

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go



# create a DataFrame from the .csv file:
df = pd.read_csv('data/mocksurvey.csv', index_col=0)
print(df)

# create traces using a list comprehension:
trace1 = go.Bar(x=df.index,
                y=df['Strongly Agree'],
                name='Strongly Agree')

trace2 = go.Bar(x=df.index,
                y=df['Somewhat Agree'],
                name='Somewhat Agree')

trace3 = go.Bar(x=df.index,
                y=df['Neutral'],
                name='Neutral')

trace4 = go.Bar(x=df.index,
                y=df['Somewhat Disagree'],
                name='Somewhat Disagree')

trace5 = go.Bar(x=df.index,
                y=df['Strongly Disagree'],
                name='Strongly Disagree')



data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(title='Survey Results', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='survey_results.html')
