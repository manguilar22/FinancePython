import dash_html_components as html
import dash_core_components as dcc
from dash import Dash

import plotly.graph_objs as go 
import statsmodels.api as sm
import pandas as pd


df = pd.read_csv("./Google.csv")
df["Date"]=pd.to_datetime(df.index)
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df.Close)
df["Close Trend"] = gdp_trend

app = Dash()

graph1=go.Scatter(x=df["Date"],y=df["Close Trend"],name="Trend Line",mode="lines")
graph2=go.Scatter(x=df["Date"],y=df["Close"],name="Close.",mode="markers")

layout00 = go.Layout(title="Hodrick - Prescott Filter")

app.layout=html.Div(children=[
dcc.Graph(id="Close-Plot",figure=dict(data=[graph1,graph2],layout=layout00))
])

if __name__ == "__main__":
    app.run_server()