from typing import Text
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re


class Company():
    def __init__(self, Symbol, start="", end="", Link_Balan = "", Link_InCome = ""):
        self.Symbol = Symbol
        self.start = start
        self.end = end
        self.Headers = {'Accept': '*/*', 'Connection': 'keepalive', 'UserAgent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
                  'AcceptEncoding': 'gzip, deflate, br', 'AcceptLanguage': 'enUS;q=0.5,en;q=0.3', 'CacheControl': 'maxage=0', 'UpgradeInsecureRequests': '1', 'Referer': 'https://google.com'}
        self.Link_Close = "https://s.cafef.vn/LichsugiaodichAAA1.chn".replace("AAA", Symbol)
        self.Link_Balan = Link_Balan
        self.Link_InCome = Link_InCome
    # thiết lập thời gian
    def set_Time(self,start,end):
        self.start = start
        self.end = end
    # thiết lập đường link
    def set_Link(self, start, end, option ="Quy"):
        arr_time = start.split("/")
        name = Company.Infor[Company.Infor["Symbol"] == self.Symbol]["Name_Company"].values[0]
        if option == "Quy":
            self.Link_Balan = "https://s.cafef.vn/baocaotaichinh/"+self.Symbol+"/IncSta/"+arr_time[2]+"/"+str(int(arr_time[1])//3+1)+"/0/0/baocaotaichinh"+name
            self.Link_InCome = "https://s.cafef.vn/baocaotaichinh/"+self.Symbol+"/BSheet/"+arr_time[2]+"/"+str(int(arr_time[1])//3+1)+"/0/0/ketquahoatdongkinhdoanh"+name
        else:
            self.Link_InCome = "https://s.cafef.vn/baocaotaichinh/"+self.Symbol+"/IncSta/"+arr_time[2]+"/0/0/0/baocaotaichinh"+name
            self.Link_Balan = "https://s.cafef.vn/baocaotaichinh/"+self.Symbol+"/BSheet/"+arr_time[2]+"/0/0/0/ketquahoatdongkinhdoanh"+name
    #Giá đóng cửa
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
    def get_One_Close(self):
        try:
            data = self.get_All_Close()
            return data.loc[len(data["close"])+1]
        except:
            return pd.DataFrame({"date":[],"close":[]})
    
    def get_Value_match(self,id_batch = 1):
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
        return stock_slice_batch["value_match"].astype(float) 
    def get_Arg_Value_Match(self):
        try:
            return self.get_Volume().mean()
        except:
            return None


    #Báo cáo tài chính
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
    
    # Số lượng cổ phiếu phát hành

    def getVolumeStart(self, link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        a_string = soup.find(string= re.compile("Khối lượng cổ phiếu niêm yết lần đầu:"))
        return a_string.parent.b.text.replace(" ",'').replace("\n","").replace(",",'')

    # def getTimeLineVolume(self):
    #     link = "https://s.cafef.vn/Ajax/Events_RelatedNews_New.aspx?symbol=AAA&floorID=0&configID=4&PageIndex=1&PageSize=200&Type=1"
    #     r = requests.get(link)
    #     soup = BeautifulSoup(r.content, 'html.parser')






















