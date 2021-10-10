import pandas as pd
# df_data = pd.read_csv("Test.csv")


# for i in range(len(df_data["Time"])):
#   if df_data["Time"][i] != "2021/2/0/0":
#     break
#   print(df_data["COMPANY"][i])
#   df_ARG = pd.read_csv("DividendVietName_Volume/ValueVolume/*.csv".replace("*",df_data["COMPANY"][i]))
#   print(df_ARG["Value Volume"][0])
#   df_data["ValueARG"][i] = df_ARG["Value Volume"][0]

# df_data.to_csv("FinalARGValue.csv")
df_data_new = pd.read_csv("FinalARGValue.csv")
df_data_old = pd.read_csv("FinalData12.csv")
df_data_old = df_data_old.drop(columns=["PRICE","BAN","VOLUME","EARNINGS","COGS","SALES","CASH","INVESTMENTS","RECEIVABLES","INVENTORY","DEBTS","VOLUME","FOMULA","Unnamed: 0","MARKET CAP","PROFIT"])
result = pd.merge(df_data_new, df_data_old, how="left",on=["Time","COMPANY"])
result.to_csv("FinalARGValue(edited).csv",index=False)
