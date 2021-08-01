from numpy.lib.shape_base import split
from base.Company import Company
import pandas as pd
pd.options.mode.chained_assignment = None

data = pd.read_excel("DATA_TEST_20h_27_5.xlsx")
data["PRICE"] = 0.0
data["BAN"] = 0.0

Companys = list(set(data["COMPANY"]))

def getIndex(arr):
  for i in arr:
    s = i.split("/")
    yield 53 - ((int(s[0])-2008)*4+int(s[1]))

for Symbol in Companys:
  print(Symbol)
  dataClose = pd.read_csv("Data_Result\*.csv".replace("*",Symbol))
  ListIndex = data[data["COMPANY"] == Symbol].index
  ListIndexClose = list(getIndex(data[data["COMPANY"] == Symbol]["Time"]))
  count = 0
  
  for index in ListIndex:
    if count < len(ListIndexClose) and ListIndexClose[count] < len(dataClose["close"])-1:
      # print(dataClose["close"][ListIndexClose[count]],index)
      data["BAN"][index] = dataClose["close"][ListIndexClose[count]]
      data["PRICE"][index] = dataClose["close"][ListIndexClose[count]+1]
      count += 1
    else:
      break
  
data.to_excel("FinanResearch.xlsx")



