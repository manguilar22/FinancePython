import quandl as q
import pandas as pd 
from datetime import datetime as d 

class Stock(object):
    
    df = None

    stock_format = ['Date',
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

    
    def __init__(self):
        print("Stock Class Accessed :\t",str(d.now()))
    
    def quandl(self,name=str,start_date=None):
        misc = ["Ex-Dividend", "Split Ratio"]
        self.df = q.get(name, start_date=start_date,end_date=d.now())
        self.df.drop(labels=misc,axis=1,inplace=True)
        self.df.index=pd.to_datetime(self.df.index)
        self.df["Date"] = self.df.index
        self.df = self.df[["Open","Close","High","Low","Volume","Adj. Open","Adj. Close","Adj. High","Adj. Low","Adj. Volume"]]
        return self.df
    
    def dataset(self):
        return self.df
    
    def save(self,fileName=str):
        save = lambda s : str(d.now()).strip().replace(" ","")+s+".csv"
        path = "../stocks/datasets/"+save(fileName)
        print("Saving CSV file in:\t{}".format(path))
        self.df = self.df[self.stock_format]
        self.df.to_csv(path,index=False)
    
    def to_text(self,dataframe=None,stockName=str):
        text=""
        path=str(d.now()).strip().replace(" ","")+stockName+".txt"
        save_dir=str("./exports/"+path)
        self.df["Date"] = pd.to_datetime(self.df.index)
        toString = lambda o,c,h,l,v,ao,ac,ah,al,av,d: "{},{},{},{},{},{},{},{},{},{},{}\n".format(d,o,c,h,l,v,ao,ac,ah,al,av)
        
        for e in range(len(dataframe)):

            text += toString(dataframe["Open"][e],
                             dataframe["Close"][e],
                             dataframe["High"][e],
                             dataframe["Low"][e],
                             dataframe["Volume"][e],
                             dataframe["Adj. Open"][e],
                             dataframe["Adj. Close"][e],
                             dataframe["Adj. High"][e],
                             dataframe["Adj. Low"][e],
                             dataframe["Adj. Volume"][e],
                             dataframe["Date"][e])   
        
        print("Stock has been saved to:\t{}".format(save_dir)) 
        with open(save_dir,"w") as f:
            f.write(text) 
            f.close()

