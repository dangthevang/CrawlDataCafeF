import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
def getData(data,field):
    for i in field:
        try:
            t = data[data[0]==i].index
            x = data[4][t].values[0]
            break
        except:
            x = 0
    return x

class Company():
    def __init__(self, Symbol, start="", end="", Link_Balan = "", Link_InCome = ""):
        self.Symbol = Symbol
        self.start = start
        self.end = end
        self.Headers = {'content-type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla'}
        self.Link_Close = "https://s.cafef.vn/Lich-su-giao-dich-AAA-1.chn".replace("AAA", Symbol)
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
        form_data = {'ctl00$ContentPlaceHolder1$scriptmanager': 'ctl00$ContentPlaceHolder1$scriptmanager|ctl00$ContentPlaceHolder1$ctl03$btSearch',
                     'ctl00$ContentPlaceHolder1$ctl03$txtKeyword': self.Symbol,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate1$txtDatePicker': self.start,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate2$txtDatePicker': self.end,
                     '__VIEWSTATEGENERATOR': '2E2252AF',
                     '__EV`ENTARGUMENT': id_batch,
                     '__ASYNCPOST': 'true'}
        r = requests.post(self.Link_Close, data=form_data,
                          headers=self.Headers, verify=True)
        print(r.content)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('table')
        stock_slice_batch = pd.read_html(str(table))[1].iloc[2:,:12]
        stock_slice_batch.columns = ['date', 'adjust', 'close', 'change_perc', 'avg',
                                     'volume_match', 'value_match', 'volume_reconcile', 'value_reconcile',
                                     'open', 'high', 'low']
        return stock_slice_batch[["date","close"]]
    def get_One_Close(self):
        # try:
            data = self.get_All_Close()
            return data
        # except:
        #     return pd.DataFrame({"date":[],"close":[]})
    
    def get_Value_match(self,id_batch = 1):
        form_data = {'ctl00$ContentPlaceHolder1$scriptmanager': 'ctl00$ContentPlaceHolder1$ctl03$panelAjax|ctl00$ContentPlaceHolder1$ctl03$pager2',
                     'ctl00$ContentPlaceHolder1$ctl03$txtKeyword': self.Symbol,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate1$txtDatePicker': self.start,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate2$txtDatePicker': self.end,
                     '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctl03$pager2',
                     '__EVENTARGUMENT': id_batch,
                     '__ASYNCPOST': 'true'}
        r = requests.post(self.Link_Close, data=form_data,
                          headers=self.Headers, verify=False)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        stock_slice_batch = pd.read_html(str(table))[0].iloc[2:,:12]
        stock_slice_batch.columns = ['date', 'adjust', 'close', 'change_perc', 'avg',
                                     'volume_match', 'value_match', 'volume_reconcile', 'value_reconcile',
                                     'open', 'high', 'low']
        return stock_slice_batch["value_match"].astype(float) 
    def get_Arg_Value_Match(self):
        try:
            return self.get_Value_match().mean()
        except:
            return None

    def get_Volume(self,id_batch = 1):
        form_data = {'ctl00$ContentPlaceHolder1$scriptmanager': 'ctl00$ContentPlaceHolder1$ctl03$panelAjax|ctl00$ContentPlaceHolder1$ctl03$pager2',
                     'ctl00$ContentPlaceHolder1$ctl03$txtKeyword': self.Symbol,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate1$txtDatePicker': self.start,
                     'ctl00$ContentPlaceHolder1$ctl03$dpkTradeDate2$txtDatePicker': self.end,
                     '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ctl03$pager2',
                     '__EVENTARGUMENT': id_batch,
                     '__ASYNCPOST': 'true'}
        r = requests.post(self.Link_Close, data=form_data,
                          headers=self.Headers, verify=False)

        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        stock_slice_batch = pd.read_html(str(table))[0].iloc[2:,:12]
        stock_slice_batch.columns = ['date', 'adjust', 'close', 'change_perc', 'avg',
                                     'volume_match', 'value_match', 'volume_reconcile', 'value_reconcile',
                                     'open', 'high', 'low']
        return stock_slice_batch["volume_match"].astype(float) 
    def get_Arg_Volume(self):
        try:
            return self.get_Volume().mean()
        except:
            return None
    #Báo cáo tài chính
    def getFinancal(self,link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table',{'id': 'tableContent'})
        financial = pd.read_html(str(table),displayed_only =False)
        return financial[0]
    
    def getBalan(self):
        return self.getFinancal(self.Link_Balan[0])
    
    def getIncom(self):
        return self.getFinancal(self.Link_InCome)

    def getField(self, dataField):
        page_BSheet = self.getBalan()
        page_IncSta = self.getIncom()
        data = page_BSheet.append(page_IncSta,ignore_index= True)
        arr = [i.replace(',','').replace(" ",'').replace("\n",'').replace("\r","").replace("\xa0","") for i in data[0]]
        data[0] = arr
        dict_result = {}
        for k,v in dataField.items():
            dict_result[k] = getData(data,v)
        return dict_result

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






















