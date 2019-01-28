import quandl as q
import pandas as pd 
from datetime import datetime as d
import os 

class Stock(object):
    
    df=None
    
    def __init__(self):
        print("Stock Class Accessed :\t",str(d.now()))
    
    def quandl(self,name=str,start_date=None):
        misc = ["Ex-Dividend", "Split Ratio"]
        self.df = q.get(name, start_date=start_date,end_date=d.now())
        self.df.drop(labels=misc,axis=1,inplace=True)
        self.df.index=pd.to_datetime(self.df.index)
        self.df["Date"] = self.df.index
        self.df = self.df[["Open","Close","High","Low","Volume","Adj. Open","Adj. Close","Adj. High","Adj. Low","Adj. Volume","Date"]]
        return self.df
    
    def dataset(self):
        return self.df
    
    def to_csv(self,name,columns=True):
        fileName = lambda s: "../stocks/"+s+str(d.now())+".csv"
        print("Writing to file:\t",str(fileName))
        self.df.to_csv(fileName(name),index=False,columns=columns,encoding="UTF-8")
        
    def current_dir(self):
        return os.getcwd()
    
    def to_text(self,dataframe=None,stockName=str):
        text=""
        path=str(d.now()).strip().replace(" ","")+stockName+".txt"
        save_dir=str("./exports/"+path+".txt")
            
        toString = lambda o,c,h,l,v,ao,ac,ah,al,av,d: "{},{},{},{},{},{},{},{},{},{},{}\n".format(o,c,h,l,v,ao,ac,ah,al,av,d)

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

