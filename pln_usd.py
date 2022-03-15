import requests
from bs4 import BeautifulSoup
import time


class Currency:
    USD_PLN = 'https://www.google.com/search?q=usd+to+pln&client=ubuntu&hs=o78&channel=fs&sxsrf=APq-' \
              'WBvoAmxF4a42kq3qlVmxnXjRWtnBfQ%3A1647104975595&ei=z9MsYpPvI4bfrgS31bigBw&oq=usd+t+pln+&gs_lcp=' \
              'Cgdnd3Mtd2l6EAMYADIGCAAQBxAeMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIABANMgQIA' \
              'BANOgcIABBHELADOgcIABCwAxBDOgQIIxAnOgUIABCABDoJCCMQJxBGEIICOgUIABCRAkoECEEYAEoECEYYAFD9IlihTWDuV2gGcA' \
              'F4AIAB3wGIAZgLkgEFMC44LjKYAQCgAQHIAQrAAQE&sclient=gws-wiz'

    EURO_PLN = 'https://www.google.com/search?q=euro+to+pln&client=ubuntu&hs=ZnT&channel=fs&sxsrf=APq-' \
               'WBsenUhAU86FNZDe1Z3MeAGIk5ALlw%3A1647104998304&ei=5tMsYtOLEuWxrgT5wJjAAw&oq=usd+to+pln&gs_lcp=Cgdnd' \
               '3Mtd2l6EAEYADIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHC' \
               'AAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQ0oECEEYAEoECEYYAFAAWABglg9oAnABeACAAQCIAQCSAQCYAQDIAQrAAQE&sclient' \
               '=gws-wiz'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    usd_price = 0
    euro_price = 0

    def __init__(self):
        self.usd_price = float(self.get_usd_price().replace(",", "."))
        self.euro_price = float(self.get_usd_price().replace(",", "."))

    def get_usd_price(self):
        full_page = requests.get(self.USD_PLN, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        return convert[0].text

    def get_euro_price(self):
        full_page = requests.get(self.EURO_PLN, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_cur(self):
        usd = float(self.get_usd_price().replace(",", "."))
        euro = float(self.get_euro_price().replace(",", "."))
        print("1 $ = " + str(usd) + " PLN")
        print("1 € = " + str(euro) + " PLN")
        print("--------------")
        time.sleep(3)
        self.check_cur()


if __name__ == "__main__":
    currency = Currency()
    currency.check_cur()
