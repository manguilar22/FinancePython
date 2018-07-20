from dash import Dash 
import dash_core_components as dcc 
import dash_html_components as html 

import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv("./../../stocks/Facebook.csv")
df["Date"] = pd.to_datetime(df.index) 

data=[
go.Scatter(x=df["Date"],y=df["Open"],mode="markers",name="Open"),
go.Scatter(x=df["Date"],y=df["Close"],mode="markers",name="Close"), 
go.Scatter(x=df["Date"],y=df["High"],mode="markers",name="High"),
go.Scatter(x=df["Date"],y=df["Low"],mode="markers",name="Low")] 
layout = go.Layout(title="Facebook Stock",xaxis=dict(title="Date"),yaxis=dict(title="Options"))
graph = dcc.Graph(id="FacebookStock",figure=dict(data=data,layout=layout))

app = Dash() 
app.layout= html.Div(children=[ 
    dcc.Markdown('''# Stocks '''), 
    graph
])

if __name__ == "__main__":
    app.run_server() 
