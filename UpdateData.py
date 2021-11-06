from base.Company import Company
import pandas as pd

from base.MergeData import MergeData
convert = MergeData(54)

data = pd.read_csv("quy1.csv")
df_close = pd.read_csv("VolumeADD.csv")
arr = []
for t in df_close["date"]:
  arr.append(convert.timeToCodeTimeBuy(t))
df_close["Time"] = arr
df_close["COMPANY"]=df_close["Symbol"]
df_close = df_close.drop(columns=["date","Symbol"])
result = pd.merge(data, df_close, how="left",on=["Time","COMPANY"])
# check_for_nan = data["ValueARG"].isnull()
result.to_csv("quy2.csv",index=False)
# arr = []

# for i in range(len(check_for_nan)):
#   if check_for_nan[i] == True:
#     arr.append(data["COMPANY"][i])

# print(list(set(arr)))


