import pandas as pd

data = pd.read_csv("HOSE_Quý_032021.csv")
close = pd.read_csv("CafeF.RAW_HSX.01.11.2021.csv")
# for i in range(len(data['COMPANY'])):
#   if data["YEAR"][i] == "2021/2/0/0":
#     try:
#       data["BAN"][i] = close[close["<Ticker>"] == data["COMPANY"][i]]["<Close>"].iloc[0]
#     except:
#       data["BAN"][i] = -1
# data.to_csv("ChuaChinhSua.csv",index = False)
arr = []
for i in range(len(data['COMPANY'])):
    try:
      arr.append(close[close["<Ticker>"] == data["COMPANY"][i]]["<Close>"].iloc[0])
    except:
      arr.append(0)
data["PRICE"] = arr

data.to_csv("Quy3.csv",index = False)
