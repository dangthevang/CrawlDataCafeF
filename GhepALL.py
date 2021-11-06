from numpy.core.fromnumeric import mean
import pandas as pd

data1 = pd.read_csv("CafeF.RAW_HSX.Upto01.11.2021.csv")
data2 = pd.read_csv("Final_02-11(Edited).csv")

# for i in range(len(data2["YEAR"])):
#   if data2["YEAR"][i] == "2021/3/0/0":
#     symbol = data2["COMPANY"][i] 
#     data_symbol = data1.query('Ticker == @symbol & DTYYYYMMDD <= 20211101 & DTYYYYMMDD >= 20211020')
#     data_symbol["ValueARG"] = data_symbol["Close"]*data_symbol["Volume"]
#     data2["ValueARG"][i] = mean(data_symbol["ValueARG"])
#     data2["VolumeARG"][i] = mean(data_symbol["Volume"])
# data2.to_csv("Final_02-11(Edited).csv")

for i in range(len(data2["YEAR"])):
  if data2["YEAR"][i] == "2021/2/0/0":
    symbol = data2["COMPANY"][i]
    print(symbol)
    data_symbol = data1.query('Ticker == @symbol & DTYYYYMMDD >= 20210806 & DTYYYYMMDD <= 20210810')
    try:
      data2["PRICE"][i] = data_symbol["Close"][data_symbol.index[-1]]
    except:
      data2["PRICE"][i] = -1
data2.to_csv("Final_02-11(Edited) Part2.csv")