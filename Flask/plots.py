import plotly.graph_objects as go
from cleaning_data import data_titanic
import json
import plotly

def grafik1():
    dfTitanic = data_titanic()
    fig = go.Figure([go.Bar(x=dfTitanic['sex'], y=dfTitanic['fare'])])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) #ubah ke json biar bisa dipake di html
    return fig_json


