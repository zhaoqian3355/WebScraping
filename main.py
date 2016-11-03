from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


fightUrl='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=DLC&ACity1=SHA&SearchType=S&DDate1=2016-11-04&IsNearAirportRecommond=0&rk=0.8936676051200609145454&CK=052284128A811F5580F548DF4AE52C1E&r=0.53111172658318670744115'

response=urlopen(fightUrl)

byteData=response.read()
# stringData=byteData.decode('gb2312')


json.dump(byteData)


with open("data.txt",'wb') as fileStream:
    fileData=fileStream.write(byteData)

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon"); 
bsObj=BeautifulSoup(html);
 
for link in bsObj.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href']);