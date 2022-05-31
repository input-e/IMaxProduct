import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from Day_object import *

def Main():
    texted = get_page()
    only_table = SoupStrainer("table")
    soup = BeautifulSoup(texted, 'html.parser', parse_only=only_table)
    my_day = Day(42, soup.tbody)


def get_page() -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    url = 'http://mgke.minsk.edu.by/ru/main.aspx?guid=3831'
    req = requests.request(method="GET", url=url, headers=headers)
    return req.text


def create_file(soup) -> None:
    with open('index.html', 'w', encoding="utf-8") as file:
        file.write(soup.prettify())


if __name__ == '__main__':
    Main()
