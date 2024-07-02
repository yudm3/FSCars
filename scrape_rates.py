import requests
from bs4 import BeautifulSoup

class GetGoogleRates:
    def __init__(self):
        self.rates = {}
        self.base_url = "https://www.google.com/finance"
        self.language = "en"
        self.symbols = ["USD-KRW", "EUR-KRW", "KRW-USD"]
        self.fetch_rates()

    def fetch_rates(self):
        for symbol in self.symbols:
            target_url = f"{self.base_url}/quote/{symbol}"
            page = requests.get(target_url)
            soup = BeautifulSoup(page.content, "html.parser")
            rate_text = soup.find("div", {"class": "YMlKec fxKbKc"}).text
            rate = float(rate_text.replace(",", ""))
            self.rates[symbol] = [rate]

    def get_rates(self):
        return self.rates