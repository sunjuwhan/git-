from cgitb import text
from distutils.log import info
import requests
from bs4 import BeautifulSoup
from enum import Enum
import re
from enum import Enum
char="★&0123456789,"
class Day(Enum):
    Mon=0
    Tue=1
    Wed=2
    Thr=3
    Fri=4
    Sat=5
    Sun=6
url="http://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=35"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
menu={0:[],1:[],2:[],3:[],4:[]}
info=soup.find_all("ul",aattrs={"clss":"menu_im"})
for day in range(0,5):   
    for mn_num in range(0,14):
        menu_index=(info[day+6].find_all("li")[mn_num].get_text())
        menu[day].append(menu_index)

day=int(input("원하는 요일을 선택하싮시오"))
for i in range(0,14):
    print(menu[day][i])
    print()


