import requests
from bs4 import BeautifulSoup
import time


class Currency:
    USD_PLN = 'https://www.google.com/search?sxsrf=ALeKk01x8cik5P-GTKaHMbP22U6vqFyZFw%3A1585144497689&ei=sWJ7Xp3ZKaiSmwWH34a4BA&q=usd+to+pln&oq=usd+to+pln&gs_l=psy-ab.3..35i39j0j0i67j0l7.1426846.1427461..1427958...0.3..0.283.528.0j2j1......0....1..gws-wiz.......0i71j0i7i30.jZYxyZPSlfI&ved=0ahUKEwjd9c6147XoAhUoyaYKHYevAUcQ4dUDCAo&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    curr_price = 0

    def __init__(self):
        self.curr_price = float(self.get_price().replace(",","."))

    def get_price(self):
        full_page = requests.get(self.USD_PLN, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_cur(self):
        cur = float(self.get_price().replace(",", "."))
        print("1 $ = " + str(cur)+" pln")
        time.sleep(3)
        self.check_cur()


currency = Currency()
currency.check_cur()
