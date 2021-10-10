import pandas as pd
from datetime import datetime

def CoverTime(arr, start=True):
  s = arr.split("/")
  if start:
    day  = str(int(s[0])+(int(s[1])*3+2)//12) +"-0" +str((int(s[1])*3+2)%12) +"-06"
  else:
    day = str(int(s[0])+(int(s[1])*3+5)//12) +"-0" +str((int(s[1])*3+5)%12) +"-01"
  if len(day)>10:
    day = day[:5]+day[6:]
  return datetime.fromisoformat(day)


def getSale(time,symbol,value):
  print(symbol)
  dividend = pd.read_csv("DividendVietName_Volume/DividendVietNam/{}.csv".format(symbol))
  start = CoverTime(time)
  end = CoverTime(time,False)
  sum = 0
  cp = 1
  if dividend.empty:
    return value
  dividend['time'] = pd.to_datetime(dividend['time'],dayfirst=True)
  for i in range(len(dividend['time'])-1,-1,-1):
    if dividend['time'][i] >= start and dividend['time'][i] <= end:
      tyle = dividend['tyle'][i]
      if dividend['tien'][i] == True:
        sum = sum + cp*10*float(tyle)/100
      else:
        cp += 1/eval(tyle.replace(":","/"))
  return value*cp+sum


data = pd.read_csv("SemiFinal.csv")
arr = []
for i in range(len(data["COMPANY"])):
    arr.append(getSale(data["Time"][i],data["COMPANY"][i],data["Ban"][i]))

data["Ban"] = arr

data.to_csv("testFinal.csv")