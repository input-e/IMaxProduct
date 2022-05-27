from typing import Dict, List
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer 


class Day():
    def __init__(self, group, table):
        self.group = group
        self.table = table
        self.day_date = self.day_date_parse(self.table)

    def day_date_parse(self, table) -> Dict:
        iteration = 0
        contain = {'day':'', 'date':''}
        while True:
            if iteration == len(table.find_all('tr')):
                raise Exception('No such number of group!')

            if len(table.find_all('tr')[iteration].find_all('td')):
                terminator_1 = table.find_all('tr')[0].find_all('td')[0].text.find('-')
                terminator_2 = table.find_all('tr')[0].find_all('td')[0].text.find(',')
                contain['day'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_1+2:terminator_2]
                contain['date'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_2+2:].rstrip()
                return contain

            iteration += 1
    
    def day_show(self):
        pass

    def part_show(self, number, details="all"):
        pass

    def show(self):
        pass


class Pare():
    def __init__(self, sell_position):
        pass
