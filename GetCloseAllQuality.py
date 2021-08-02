from base.Company import Company
import pandas as pd
import time
def CoverTime(Quality,start = True):
  if start == True:
    return "01/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))
  else:
    return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))

Symbol = pd.read_csv("base/CafeF_HOSE.csv")

for symbol in Symbol['Symbol']:
  data_close = pd.DataFrame({"date":[],"close":[]})
  Quality = 54
  while Quality != 0:
    try:
      Quality -= 1
      start = CoverTime(Quality)
      end = CoverTime(Quality,False)
      data = Company(symbol,start,end)
      data_close = data_close.append(data.get_One_Close())
    except:
      # Quality -= 1
      continue
  data_close.to_csv('Ban\*'.replace("*",symbol+".csv"),index=False)
  print(symbol)


