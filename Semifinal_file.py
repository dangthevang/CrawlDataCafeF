import pandas as pd
from pandas.core.frame import DataFrame

df_symbol = pd.read_excel("SymbolCanGhep.xlsx")

data = pd.DataFrame({})
for i in df_symbol["Symbol"]:
  df_semifinal = pd.read_csv("Sale/*.csv".replace("*",i))
  df_semifinal["COMPANY"] = [i for t in df_semifinal["Time"]]
  data = data.append(df_semifinal)
data.to_csv("SemiFinal.csv")