import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()

fig = px.scatter(df,x="sepal_length", y = "sepal_width", color = "species")

#fig.show()

pyo.plot(fig, filename = 'Mi_Gráfica_de_dispersion.html')