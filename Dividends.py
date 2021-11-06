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
  dividend = pd.read_csv("Dividend(11-02-2021)\Dividend(11-02-2021)\{}.csv".format(symbol))
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
        cp += cp*1/eval(tyle.replace(":","/"))
  print(symbol,value,value*cp+sum)
  return value*cp+sum


data = pd.read_csv("ChuaChinhSua.csv")
arr = []
for i in range(len(data["COMPANY"])):
    if data["YEAR"][i] == "2021/2/0/0":
      data["BAN"][i] = getSale(data["YEAR"][i],data["COMPANY"][i],data["BAN"][i])


data.to_csv("testFinal.csv")