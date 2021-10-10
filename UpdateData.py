from base.Company import Company
import pandas as pd


data = pd.read_csv("FinalARGValueedited-1.csv")

check_for_nan = data["ValueARG"].isnull()

arr = []

for i in range(len(check_for_nan)):
  if check_for_nan[i] == True:
    arr.append(data["COMPANY"][i])

print(list(set(arr)))


