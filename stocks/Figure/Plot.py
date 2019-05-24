import plotly.graph_objs as go
from dash_table import DataTable
from pandas import DataFrame

class Figure:


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
        :return: tuple of plots
        """
        ohlc = go.Ohlc(
            x=dataframe["Date"],
            open=dataframe["Open"],
            close=dataframe["Close"],
            high=dataframe["High"],
            low=dataframe["Low"]
        )
        # Missing Candlestick
        return ohlc