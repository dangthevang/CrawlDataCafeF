import pandas as pd
from base.MergeData import MergeData

path = "C:/Users/lenovo/Desktop/CrawlCafeF/CrawlDataCafeF/Sale"
df_symbol = pd.read_excel("SymbolCanGhep.xlsx")
convert = MergeData(54)



for i in df_symbol["Symbol"]:
  print(i)
  df_com = pd.read_csv("Price/*.csv".replace("*",i))
  df_close = pd.read_csv("Ban/*.csv".replace("*",i))
  df_close_1 = pd.read_csv("Ban1/*.csv".replace("*",i))
  arr = []
  for t in df_close["date"]:
    arr.append(convert.timeToCodeTimeSale(t))
  df_close["Time"] = arr
  df_close["Ban"] = df_close["close"]
  df_close = df_close.drop(columns=["date","close"])
  result = pd.merge(df_com, df_close, how="left",on=["Time"])

  result["Ban"][0] =df_close_1["close"][0]

  # arr = []
  # for t in df_close_1["date"]:
  #   arr.append(convert.timeToCodeTimeSale(t))
  # df_close_1["Time"] = arr
  # df_close_1["Ban"] = 
  # df_close_1 = df_close_1.drop(columns=["date","close"])
  # result = pd.merge(result, df_close_1, how="left",on=["Time"])

  p = path+"/*.csv".replace("*",i)
  result.to_csv(p,index=False)