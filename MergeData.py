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

# dataClose = pd.read_csv("Data_Result_Mua\*.csv".replace("*","AAA"))
# ListIndex = data[data["COMPANY"] == "AAA"].index
# ListIndexClose = list(getIndex(data[data["COMPANY"] == "AAA"]["Time"]))
# print(ListIndexClose)

for Symbol in Companys:
  print(Symbol)
  dataClose = pd.read_csv("Data_Result_Mua\*.csv".replace("*",Symbol))
  ListIndex = data[data["COMPANY"] == Symbol].index
  ListIndexClose = list(getIndex(data[data["COMPANY"] == Symbol]["Time"]))
  count = 0
  
  for index in ListIndex:
    if count < len(ListIndexClose) and ListIndexClose[count] < len(dataClose["close"])-1:
      if ListIndexClose[count] == 0:
        data["BAN"][index] = -1
        data["PRICE"][index] = dataClose["close"][ListIndexClose[count]]
      else:
        data["BAN"][index] = dataClose["close"][ListIndexClose[count]-1]
        data["PRICE"][index] = dataClose["close"][ListIndexClose[count]]
      count += 1
    else:
      break
  
data.to_excel("FinalResearch.xlsx")



