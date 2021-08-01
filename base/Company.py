import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Company():
    def __init__(self, Symbol, start, end, option ="Quy"):
        self.Symbol = Symbol
        self.start = start
        self.end = end
        self.option = option
        self.Headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
                  'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}
        self.Link_Close = "https://s.cafef.vn/Lich-su-giao-dich-AAA-1.chn".replace("AAA", Symbol)
        self.Link_Balace_Financal = ""
        self.Link_InCome_Financal = ""

    def get_One_Close(self):
      data = self.get_All_Close()
      return data.loc[len(data["close"])]
    
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
    
    # def Create()


    
