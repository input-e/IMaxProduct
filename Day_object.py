from pickletools import int4
from typing import Dict, List
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer 


class Day():
    def __init__(self, group: int, table):
        self.group = group
        self.day_date = self.day_date_parse(table)
        self.subject = self.subject_parse(table)
        

    def day_date_parse(self, table ) -> Dict:
        contain = {'day':'', 'date':''}
        for iteration in range(0, len(table.find_all('tr'))-1):
            if len(table.find_all('tr')[iteration].find_all('td')):
                terminator_1 = table.find_all('tr')[0].find_all('td')[0].text.find('-')
                terminator_2 = table.find_all('tr')[0].find_all('td')[0].text.find(',')
                contain['day'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_1+2:terminator_2]
                contain['date'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_2+2:].rstrip()
                return contain
        
        if contain['day'] == '' or contain['date'] == '':
            raise Exception('There is no information about day and data')

    
    def subject_parse(self, table) ->list:

        def eject_data(row: int, column: int, table) ->list:

            def define_len(row):
                len = row+1
                a = 0
                while table.find_all('tr')[len+1].find('td').text.strip() == str(a+1):
                    len += 1
                    a += 1
                return len

            list = []
            for iteration in range(row+2, define_len(row)+1):
                num = int(table.find_all('tr')[iteration].find('td').text.strip())                  #return number of subject
                mn_cnt = table.find_all('tr')[iteration].find_all('td')[(column*2)-1].text.strip()  #return main content of subject
                class_num = table.find_all('tr')[iteration].find_all('td')[(column*2)].text         #return number or numbers of classrooms
                list.append(Pare(number = num, main_content = mn_cnt, classroom_number=class_num)) # create the object of subject which contained in item of list

            return list

         # search for the position of group number in row
        def find_position(table) ->int:
            for r in range(0, len(table.find_all('tr'))-1):
                if table.find_all('tr')[r].find('td').text.strip() == '№':
                    for col in range(1, len(table.find_all('tr')[r].find_all('td'))):
                        if table.find_all('tr')[r].find_all('td')[col].text.strip() == str(self.group):
                            return r, col

            raise Exception('No such grop number here')

        
        row, column = find_position(table)
        return eject_data(row, column, table)

        
    def show(self):
        print(f'Number of group: {self.group}\n')
        print('Date: ' + self.day_date['date'] + '\tDay: ' + self.day_date['day'] + '\n')
        for i in range(0, len(self.subject)):
            print('############################################')
            print(self.subject[i].number)
            print('___________________')
            print(self.subject[i].main_content)
            print('\n___________________')
            print(self.subject[i].classroom_number)
            print('\n___________________')


class Pare():
    def __init__(self, number: int, main_content: str, classroom_number):
        self.number = number
        self.main_content = main_content
        self.classroom_number = classroom_number
