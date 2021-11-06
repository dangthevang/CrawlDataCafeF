
from multiprocessing.context import Process
from base.Company import Company
import pandas as pd


def CoverTime(Quality,start = True):
  if start == True:
    return "01/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))
  else:
    return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))


def xuli(symbol):
  data_close = pd.DataFrame({"date":[],"close":[]})
  Quality = 55
  data = Company(symbol)
  data.start = CoverTime(Quality)
  data.end = CoverTime(Quality,False)
  print(data.start,data.end,data.get_One_Close())
  v = 5
  # while data_close.empty and v >0:
  #   v-=1
  #   data_close = data_close.append(data.get_One_Close())
  # data_close.to_csv('Ban(11-02)\*'.replace("*",symbol+".csv"),index=False)
  # print(symbol)
#   Symbol = pd.read_csv("base/CafeF_HOSE.csv")
# for symbol in Symbol['Symbol']:
if __name__ == '__main__':
  # pd.read_csv("base/CafeF_HOSE.csv")
  Symbol = ["AAA"]
  process = []
  for symbol in Symbol:
    proc = Process(target=xuli,args=(symbol,))
    process.append(proc)
    proc.start()
  for p in process:
    p.join()

