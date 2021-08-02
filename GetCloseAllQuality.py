
from multiprocessing.context import Process
from base.Company import Company
import pandas as pd
import multiprocessing as mp


def CoverTime(Quality,start = True):
  if start == True:
    return "01/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))
  else:
    return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))


def xuli(symbol):
  data_close = pd.DataFrame({"date":[],"close":[]})
  Quality = 54
  data = Company(symbol)
  while Quality != 0:
    try:
      Quality -= 1
      data.start = CoverTime(Quality)
      data.end = CoverTime(Quality,False)
      data_close = data_close.append(data.get_One_Close())
    except:
      continue
  data_close.to_csv('Ban\*'.replace("*",symbol+".csv"),index=False)
  print(symbol)

if __name__ == '__main__':
  Symbol = pd.read_csv("base/CafeF_HOSE.csv")
  process = []
  for symbol in Symbol['Symbol']:
    proc = Process(target=xuli,args=(symbol,))
    process.append(proc)
    proc.start()
  for p in process:
    p.join()
# a = Company.CreateCompany("AAA","05/03/2018","05/12/2018","Q")
# print(a.getBalan())
