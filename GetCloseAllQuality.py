from base.Company import Company
import pandas as pd
import time
def CoverTime(Quality,start = True):
  if start == True:
    return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))
  else:
    return "15/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))

Symbol = pd.read_csv("base\CafeF_HOSE.csv")

for symbol in Symbol['Symbol']:
  data_close = pd.DataFrame({"date":[],"close":[]})
  Quality = 54
  time.sleep(1)
  while Quality != 0:
    try: 
      Quality -= 1
      start = CoverTime(Quality)
      end = CoverTime(Quality,False)
      data = Company(symbol,start,end)
      data_close = data_close.append(data.get_One_Close())
    except:
      Quality = 0
  data_close.to_csv('Data_Result\*'.replace("*",symbol+".csv"),index=False)
  print(symbol)


