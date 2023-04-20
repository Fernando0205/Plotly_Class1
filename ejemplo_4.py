import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(52)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#Mi primer pedazo de información


data = [
    go.Scatter(x=random_x, y= random_y, mode = 'markers')
]

layout = go.Layout(
    title = 'Mi plot', xaxis = {'title':'Eje x'},
    yaxis = dict(title = 'Eje y'), hovermode = 'closest'
)

fig = go.Figure(data = data, layout=layout)

fig.show()