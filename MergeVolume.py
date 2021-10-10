import pandas as pd
path = "C:/Users/lenovo/Desktop/CrawlCafeF/CrawlDataCafeF/VvsR"
df_symbol = pd.read_excel("SymbolCanGhep.xlsx")

# df_com = pd.read_excel("Data-Quy-HOSE-2021/*.xlsx".replace("*","AAA"))
# df_volume = pd.read_csv("Volume/*.csv".replace("*","AAA"))

# result = pd.merge(df_com, df_volume,how="left", on=["Time"])

# p = path+"/*.csv".replace("*","AAA")
# result.to_csv(p,index=False)


for i in df_symbol["Symbol"]:
  print(i)
  df_com = pd.read_excel("Data-Quy-HOSE-2021/*.xlsx".replace("*",i))
  df_volume = pd.read_csv("Volume/*.csv".replace("*",i))
  
  result = pd.merge(df_com, df_volume, on=["Time"])

  p = path+"/*.csv".replace("*",i)
  result.to_csv(p,index=False)