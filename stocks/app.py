import dash_html_components as html
import dash_core_components as dcc
from dash import Dash
from dash_table import DataTable
import plotly.graph_objs as go

import pandas as pd

stock_format = [    'Date',
                    'Open',
                    'Close',
                    'High',
                    'Low',
                    'Volume',
                    'Adj. Open',
                    'Adj. Close',
                    'Adj. High',
                    'Adj. Low',
                    'Adj. Volume',
               ]

df = pd.read_csv("./datasets/amazon.csv")
df = df[stock_format]

app = Dash()

table00 = DataTable(id="mytable",
                    columns=[dict(id=e,label=e) for e in df.columns],
                    data=df.head().to_dict("records"))

fig00 = go.Ohlc(x=df["Date"],
                open=df["Open"],
                close=df["Close"],
                high=df["High"],
                low=df["Low"])

fig01 = go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

app.layout = html.Div([
    html.H1("Plotly"),
    table00,
    html.H1("Ohlc"),
    dcc.Graph(id="ohlc",figure=dict(data=[fig00])),
    html.H1("Candlestick"),
    dcc.Graph(id="candlestick",figure=dict(data=[fig01]))
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=5000,debug=True)