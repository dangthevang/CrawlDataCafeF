from pandas.core.frame import DataFrame
from base.Company import Company
import pandas as pd
data = pd.read_csv("base/CafeF_HOSE.csv")
arr_symbol = []
arr_volume = []
for i in range(len(data["Symbol"])):
  com = Company(data["Symbol"][i])
  arr_symbol.append(data["Symbol"][i])
  print(i)
  try:
    arr_volume.append(com.getVolumeStart(data["Link"][i]))
  except:
    arr_volume.append(0)

df = pd.DataFrame({"Symbol":arr_symbol,
                    "Volume": arr_volume})
df.to_csv("VolumeFrist.csv")

# com = Company("AAM")
# t = com.getVolumeStart("http://s.cafef.vn/hose/AAM-cong-ty-co-phan-thuy-san-mekong.chn")
# print(t)