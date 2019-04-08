import plotly.graph_objs as go
import dash_table as dt
from pandas import DataFrame

class Figure(object):

    def __init__(self):
        pass

    def spread_sheet(self,id=str,dataframe=None):
        table = dt.DataTable(
            id=id,
            columns=[dict(id=e,label=e) for e in dataframe.columns],
            data=dataframe.head().to_dict("records")
        )
        return table

    def scatter(self,id=str,df=None):
        graph0 = go.Scatter(x=df["Date"], y=df["Close"], name="Close.", mode="markers",
                            marker=dict(symbol="triangle-down", color="red"))
        graph1 = go.Scatter(x=df["Date"], y=df["Open"], name="Open.", mode="markers",
                            marker=dict(symbol="triangle-up", color="green"))
        return [graph0,graph1]

    def finance(self,df=None):
        """
        :param df: is a dataframe with finance features
        :return: two graph objects will be a ohlc and candlestick
        """
        ohlc = go.Ohlc(x=df["Date"], open=df["Open"], close=df["Close"], high=df["High"], low=df["Low"])
        candlestick = go.Candlestick(x=df["Date"], open=df["Open"], close=df["Close"], high=df["High"], low=df["Low"])
        return [ohlc],[candlestick]
