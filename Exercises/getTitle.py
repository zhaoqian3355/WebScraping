import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=DLC&ACity1=SHA&SearchType=S&DDate1=2016-09-06';

def getTitle(url):
    try:
        html=urlopen(url);
    except HTTPError as e:
        return None;
    
    try:
        bsObj=BeautifulSoup(html.read());
        title=bsObj.body.h1;
    except AttributeError as e:
        return e;
    
    return title;


# title=getTitle("http://pythonscraping.com/pages/page1.html");
# if title==None:
#     print("title could not be found");
# else:
#     print(title);

