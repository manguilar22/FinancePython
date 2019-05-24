import plotly.graph_objs as go
from dash_table import DataTable
import dash_core_components as dcc

class Figure(object):


    def __init__(self):
        pass


    def to_table(self,id=str,dataframe=None,n=5):
        """
        Return Data Table with no css
        :param id: id for html tag that will render the table
        :param dataframe: dataset that will be converted to data table
        :param n: number of rows that will be rendered
        :return: Dash's data table
        """
        table = DataTable(id=id,
                          columns=[dict(id=e,label=e) for e in dataframe.columns],
                          data=dataframe.head(n).to_dict("records"))
        return table


    def to_finance(self,dataframe=None):
        """
        Financial Plots. Candlesticks and Ohlc
        :param dataframe: Dataset with time-series
        :return: tuple of plots (candlestick,ohlc)
        """
        ohlc = go.Ohlc(
            x=dataframe["Date"],
            open=dataframe["Open"],
            close=dataframe["Close"],
            high=dataframe["High"],
            low=dataframe["Low"]
        )
        candlestick = go.Candlestick(x=dataframe['Date'],
                                     open=dataframe['Open'],
                                     high=dataframe['High'],
                                     low=dataframe['Low'],
                                     close=dataframe['Close'])

        ohlcFinal = dcc.Graph(figure=dict(data=[ohlc]))
        candlestickFinal = dcc.Graph(figure=dict(data=[candlestick]))

        return (candlestickFinal,ohlcFinal)


    def to_ohlc(self,id=str,dataframe=None):
        ohlc = go.Ohlc(
            x=dataframe["Date"],
            open=dataframe["Open"],
            close=dataframe["Close"],
            high=dataframe["High"],
            low=dataframe["Low"]
        )
        final = dcc.Graph(id=id,figure=dict(data=[ohlc]))
        return final


    def to_candlestick(self,id=str,dataframe=None):
        candlestick = go.Candlestick(x=dataframe['Date'],
                                     open=dataframe['Open'],
                                     high=dataframe['High'],
                                     low=dataframe['Low'],
                                     close=dataframe['Close'])
        final = dcc.Graph(id=id,figure=dict(data=[candlestick]))
        return final


    def to_scatter(self,id=str,dataframe=None):
        """
        Scatter Plot of Open and Close features of a stock
        :param id: id for html tag that will render the table
        :param dataframe: dataset that will be plotted
        :return: a list of plotly graphs
        """
        graph0 = go.Scatter(x=dataframe["Date"],
                            y=dataframe["Close"],
                            name="Close.",
                            mode="markers",
                            marker=dict(symbol="triangle-down", color="red"))

        graph1 = go.Scatter(x=dataframe["Date"],
                            y=dataframe["Open"],
                            name="Open.",
                            mode="markers",
                            marker=dict(symbol="triangle-up", color="green"))
        graph = dcc.Graph(id=id,figure=dict(data=[graph0,graph1]))
        return graph
