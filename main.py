from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

# html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj=BeautifulSoup(html)
 
# for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
#                         href=re.compile("^(/wiki/)((?!:).)*")):
#     if 'href' in link.attrs['href']:
#         print(link.attrs['href'])


html=urlopen("https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-11-06&from_station=DLT&to_station=JNK")
bsObj=BeautifulSoup(html)
 
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                        href=re.compile("^(/wiki/)((?!:).)*")):
    if 'href' in link.attrs['href']:
        print(link.attrs['href'])