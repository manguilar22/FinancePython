import dash_html_components as html
import dash_core_components as dcc
from dash import Dash
from dash_table import DataTable
import plotly.graph_objs as go

import pandas as pd
from Figure.Figure import Figure

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

table = Figure().to_table("my-table",df)
ohlc = Figure().to_ohlc("my-ohlc",df)
candle = Figure().to_candlestick("my-candle",df)
scatter = Figure().to_scatter("my-scatter",df)

app.layout = html.Div([
    html.H1("Plotly"),
    table,
    html.H1("Ohlc"),
    ohlc,
    html.H1("Candlestick"),
    candle,
    html.H1("Scatter Plot"),
    scatter
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=5000,debug=True)