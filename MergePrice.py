import pandas as pd
from base.MergeData import MergeData

path = "C:/Users/lenovo/Desktop/CrawlCafeF/CrawlDataCafeF/Price"
df_symbol = pd.read_excel("SymbolCanGhep.xlsx")
convert = MergeData(54)



for i in df_symbol["Symbol"]:
  print(i)
  df_com = pd.read_csv("VvsR/*.csv".replace("*",i))
  df_close = pd.read_csv("Mua/*.csv".replace("*",i))
  arr = []
  for t in df_close["date"]:
    arr.append(convert.timeToCodeTimeBuy(t))
  df_close["Time"] = arr
  df_close["Mua"] = df_close["close"]
  df_close = df_close.drop(columns=["date","close"])
  result = pd.merge(df_com, df_close, how="left",on=["Time"])
  p = path+"/*.csv".replace("*",i)
  result.to_csv(p,index=False)