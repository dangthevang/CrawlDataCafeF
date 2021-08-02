import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class Company():
    # Infor = pd.read_csv("base/CafeF_HOSE.csv")
    def __init__(self, Symbol, start="", end="", Link_Balan = "", Link_InCome = ""):
        self.Symbol = Symbol
        self.start = start
        self.end = end
        self.Headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
                  'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}
        self.Link_Close = "https://s.cafef.vn/Lich-su-giao-dich-AAA-1.chn".replace("AAA", Symbol)
        self.Link_Balan = Link_Balan
        self.Link_InCome = Link_InCome
    
    @classmethod
    def CreateCompany(cls,Symbol, start, end, option ="Quy"):
        arr_time = start.split("/")
        name = Company.Infor[Company.Infor["Symbol"] == Symbol]["Name_Company"].values[0]
        if option == "Quy":
            LinkInCome = "https://s.cafef.vn/bao-cao-tai-chinh/"+Symbol+"/IncSta/"+arr_time[2]+"/"+str(int(arr_time[1])//3+1)+"/0/0/bao-cao-tai-chinh-"+name
            LinkBalan = "https://s.cafef.vn/bao-cao-tai-chinh/"+Symbol+"/BSheet/"+arr_time[2]+"/"+str(int(arr_time[1])//3+1)+"/0/0/ket-qua-hoat-dong-kinh-doanh-"+name
        else:
            LinkInCome = "https://s.cafef.vn/bao-cao-tai-chinh/"+Symbol+"/IncSta/"+arr_time[2]+"/0/0/0/bao-cao-tai-chinh-"+name
            LinkBalan = "https://s.cafef.vn/bao-cao-tai-chinh/"+Symbol+"/BSheet/"+arr_time[2]+"/0/0/0/ket-qua-hoat-dong-kinh-doanh-"+name
        return cls(Symbol, start, end,LinkBalan,LinkInCome)

    def get_One_Close(self):
        try:
            data = self.get_All_Close()
            return data.loc[len(data["close"])+1]
        except:
            return {"date":-1.0,"close":-1.0}
    
    def get_All_Close(self,id_batch = 1):
        form_data = {'ctl00$ContentPlaceHolder1$scriptmanager': 'ctl00$ContentPlaceHolder1$ctl03$panelAjax|ctl00$ContentPlaceHolder1$ctl03$pager2',
                     'ctl00$ContentPlaceHolder1$ctl03$txtKeyword': self.Symbol,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate1$txtDatePicker': self.start,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate2$txtDatePicker': self.end,
                     '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctl03$pager2',
                     '__EVENTARGUMENT': id_batch,
                     '__ASYNCPOST': 'true'}
        r = requests.post(self.Link_Close, data=form_data,
                          headers=self.Headers, verify=True)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        stock_slice_batch = pd.read_html(str(table))[0].iloc[2:,:12]
        stock_slice_batch.columns = ['date', 'adjust', 'close', 'change_perc', 'avg',
                                     'volume_match', 'value_match', 'volume_reconcile', 'value_reconcile',
                                     'open', 'high', 'low']
        return stock_slice_batch[["date","close"]]
    
    def getFinancal(self,link):
        r = requests.get(link,
                          headers=self.Headers)
        
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table',{'id': 'tableContent'})
        financial = pd.read_html(str(table),displayed_only =False)
        return financial
    
    def getBalan(self):
        return self.getFinancal(self.Link_Balan)
    
    def getIncom(self):
        return self.getFinancal(self.Link_InCome)

    
