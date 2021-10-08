
# from multiprocessing.context import Process
# from base.Company import Company
# import pandas as pd


# def CoverTime(Quality,start = True):
#   if start == True:
#     return "01/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))
#   else:
#     return "05/m/y".replace("y",str(2008+Quality//4)).replace("m",str((Quality%4)*3+2))


# def xuli(symbol):
#   data_close = pd.DataFrame({"date":[],"close":[]})
#   Quality = 54
#   data = Company(symbol)
#   while Quality != 0:
#     try:
#       Quality = 1
#       data.start = CoverTime(Quality)
#       data.end = CoverTime(Quality,False)
#       data_close = data_close.append(data.get_One_Close())
#     except:
#       continue
#   data_close.to_csv('Ban\*'.replace("*",symbol+".csv"),index=False)
#   print(symbol)
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
# a = Company.CreateCompany("AAA","05/03/2018","05/12/2018","Q")
# print(a.getBalan())

from base.Company import Company
import requests
import pandas as pd
def create_URL(code,nameCompany,time,IncSta):
    # create URL
    s = 'https://s.cafef.vn/bao-cao-tai-chinh/NKG/IncSta/2020/4/0/0/bao-cao-tai-chinh-cong-ty-co-phan-thep-nam-kim.chn'
    if IncSta == False:
          URL = s.replace("NKG",code).replace("cong-ty-co-phan-thep-nam-kim.chn",nameCompany).replace("2020/4/0/0",time).replace("IncSta","BSheet")
    else:
          URL = s.replace("NKG",code).replace("cong-ty-co-phan-thep-nam-kim.chn",nameCompany).replace("2020/4/0/0",time)
    return URL
Data_Link_Company = pd.read_csv("base/CafeF_HOSE.csv")
def resetDef():
    data_final = pd.DataFrame({      'Time': [],
                                     'Reported_Earnings':[],
                                     'COGS':[],
                                     'Sales':[],
                                     'Cash':[],
                                     'Investments':[],
                                     'Receivable':[],
                                     'Inventory':[],
                                     'Debts':[],
                                    'Volume':[]
                                    })
    return data_final

symbol = Data_Link_Company["Symbol"][1]
name = Data_Link_Company["Name_Company"][1]
com = Company(Symbol = symbol)
data_symbol = resetDef()
quarter = 51
# while quarter >= 0:
time = str(2008+quarter//4)+"/"+str(quarter%4+1)+"/0/0"
com.Link_Balan = create_URL(symbol,name,time,False),
com.Link_InCome  = create_URL(symbol,name,time,True)

dict_field = {
  'Reported_Earnings':'18.Lợinhuậnsauthuếthunhậpdoanhnghiệp',
  'COGS':"4.Giávốnhàngbán",
  'Sales':"3.Doanhthuthuầnvềbánhàngvàcungcấpdịchvụ",
  'Cash':"1.Tiềnvàcáckhoảntươngđươngtiền",
  'Investments':"2.Cáckhoảnđầutưtàichínhngắnhạn",
  'Receivable':"3.Cáckhoảnphảithungắnhạn",
  'Inventory':"4.Hàngtồnkho",
  'Debts':"1.Nợngắnhạn",
  'Volume':"-Cổphiếuphổthôngcóquyềnbiểuquyết",
}

print(com.getField(dict_field))