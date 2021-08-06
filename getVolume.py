from base.Company import Company
import pandas as pd
import time
# data = pd.read_csv("base\CafeF_HOSE.csv")

def CoverTime(Quality,start = True):
  if start == True:
    return "20/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+1))
  else:
    return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))


def xuli(symbol):
  data_volume = pd.DataFrame({"date":[],"Volume":[]})
  Quality = 54
  data = Company(symbol)
  while Quality != 0:
    try:
      Quality -= 1
      data.start = CoverTime(Quality)
      data.end = CoverTime(Quality,False)
      data_volume = data_volume.append({"date":data.end,"Volume":data.get_Arg_Volume()},ignore_index=True)
    except:
      continue
  data_volume.to_csv('Volume\*'.replace("*",symbol+".csv"),index=False)
  print(symbol)

xuli("AAA")
# #   Symbol = pd.read_csv("base/CafeF_HOSE.csv")
# # for symbol in Symbol['Symbol']:
# if __name__ == '__main__':
#   # pd.read_csv("base/CafeF_HOSE.csv")
#   Symbol = ["AAA"]
#   process = []
#   for symbol in Symbol:
#     proc = Process(target=xuli,args=(symbol,))
#     process.append(proc)
#     proc.start()
#   for p in process:
#     p.join()
# # a = Company.CreateCompany("AAA","05/03/2018","05/12/2018","Q")
# # print(a.getBalan())
