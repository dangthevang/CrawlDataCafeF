from numpy.lib.shape_base import split
from base.Company import Company
import pandas as pd
pd.options.mode.chained_assignment = None

data = pd.read_excel("DATA_TEST_20h_27_5.xlsx")
data["PRICE"] = -1.0
data["BAN"] = -1.0

Companys = list(set(data["COMPANY"]))

def getIndex(arr):
  for i in arr:
    s = i.split("/")
    yield 53 - ((int(s[0])-2008)*4+int(s[1]))

def getClose(data,CodeTime,Ban = True):
  s = CodeTime.split("/")
  if Ban == True:
    t = int(s[1])*3+5
  else:
    t = int(s[1])*3+2
  y = "m/y".replace("y",str(int(s[0])+t//12)).replace("m",str(t%12))
  
  for i in range(len(data["close"])):
    if data["date"][i].find(y) !=-1:
      return data["close"][i]
  return -1

for Symbol in Companys:
  print(Symbol)
  dataPrice = pd.read_csv("Price\*.csv".replace("*",Symbol))
  dataBan = pd.read_csv("Ban\*.csv".replace("*",Symbol))
  ListIndex = data[data["COMPANY"] == Symbol].index
  ListIndexClose = list(getIndex(data[data["COMPANY"] == Symbol]["Time"]))
  count = 0
  
  for index in range(len(ListIndex)):
    # if count < len(ListIndexClose) and ListIndexClose[count] < len(dataPrice["close"])-1:
      # if ListIndexClose[count] == 0:
      #   data["BAN"][ListIndex[index]] = -1
      #   data["PRICE"][ListIndex[index]] = getClose(dataPrice,data["Time"][ListIndex[index]+1])
      # else:
      data["BAN"][ListIndex[index]] = getClose(dataBan,data["Time"][ListIndex[index]])
      data["PRICE"][ListIndex[index]] = getClose(dataPrice,data["Time"][ListIndex[index]],False)
      # count += 1
    # else:
    #   break
  
data.to_excel("FinalResearch.xlsx")



