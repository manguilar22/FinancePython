import quandl as q
import pandas as pd 
from datetime import datetime as d

class Stock:
    
    df=None
    
    def __init__(self):
        print("Stock Class Accessed :\t",str(d.now()))
    
    def quandl(self,name=str,start_date=None):
        misc = ["Ex-Dividend", "Split Ratio"]
        self.df = q.get(name, start_date=start_date,end_date=d.now())
        self.df.drop(labels=misc,axis=1,inplace=True)
        self.df.index=pd.to_datetime(self.df.index)
        self.df["Date"] = self.df.index
        return self.df
    
    def dataset(self):
        return self.df
    
    def to_csv(self,name,columns=True):
        fileName = lambda s: "./stocks/"+s+str(d.now())+".csv"
        print("Writing to file:\t",str(fileName))
        self.df.to_csv(fileName(name),index=False,columns=columns,encoding="UTF-8")

    def to_text(self,name,stockName=str):
        text=""
        path=str(d.now()).strip().replace(" ","")+"\n"
        save=str("\t./exports/"+path+stockName+".txt")
        f = lambda O, H, L, C, V, AO, AH, AL, AC, AV: str("{Open},{High},{Low},{Close},{Volume},{AdjOpen},\
                                                 {AdjHigh},{AdjLow},{AdjClose},{AdjVolume}\n").format(Open=O,
                                                                                                      High=H,
                                                                                                      Low=L,
                                                                                                      Close=C,
                                                                                                      Volume=V,
                                                                                                      AdjOpen=AO,
                                                                                                      AdjHigh=AH,
                                                                                                      AdjLow=AL,
                                                                                                      AdjClose=AC,
                                                                                                      AdjVolume=AV)
        for i in range(len(name)):
            text+=f(name["Open"][i],name["High"][i],name["Low"][i],
                    name["Close"][i],name["Volume"][i],name["Adj. Open"][i],
                     name["Adj. High"][i],name["Adj. Low"][i],name["Adj. Close"][i],
                     name["Adj. Volume"][i])
        print("Saved in:\t",save)
        with open(save,"w") as f:
            f.write(path)
            f.write(text)
            f.close()


