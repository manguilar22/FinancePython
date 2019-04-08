import dash_html_components as html
import dash_core_components as dcc
from dash import Dash
from dash_table import DataTable
import plotly.graph_objs as go 
import statsmodels.api as sm
import pandas as pd

from Figure.Figure import *

df = pd.read_csv("./Google.csv")
df["Date"]=pd.to_datetime(df.index)
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df.Close)
df["Close Trend"] = gdp_trend

app = Dash()

graph1=go.Scatter(x=df["Date"],y=df["Close Trend"],name="Trend Line",mode="lines",line=dict(dash="dot"))
graph2=go.Scatter(x=df["Date"],y=df["Close"],name="Close.",mode="markers",marker=dict(symbol="triangle-down",color="red"))
graph3=go.Scatter(x=df["Date"],y=df["Open"],name="Open.",mode="markers",marker=dict(symbol="triangle-up",color="green"))

candle=go.Ohlc(x=df["Date"],open=df["Open"],close=df["Close"],high=df["High"],low=df["Low"])
candle2=go.Candlestick(x=df["Date"],open=df["Open"],close=df["Close"],high=df["High"],low=df["Low"])
table = DataTable(id="table",columns=[dict(id=e,label=e) for e in df.columns],data=df.head().to_dict("records"))

# Demo OHLC and Candle
o,c = Figure().finance(df=df)


layout00 = go.Layout(title="Hodrick - Prescott Filter")
layout01 = go.Layout(xaxis = dict(rangeslider = dict(visible = False)))

app.layout=html.Div(children=[
    html.H1("Dash - Data Table"), 
    Figure().spread_sheet(id="table",dataframe=df),
    html.Hr(), 
    html.H1("Close Trend Line"),
    dcc.Graph(id="Close-Plot",figure=dict(data=[graph1,graph2,graph3],layout=layout00)),
    html.Hr(),
    html.H1("Ohlc Chart"),
    dcc.Graph(id="ohlc",figure=dict(data=c)),
    html.Hr(),
    html.H1("Candle Stick"),
    dcc.Graph(id="candlestick",figure=dict(data=o)),
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=5000)
