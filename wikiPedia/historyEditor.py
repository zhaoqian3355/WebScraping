from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now)
def getLinks(articleUrl):
    html=urlopen("http://en.wikipedia.org/"+articleUrl)
    bsObj=BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    #Format of revision history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL@action=history
    pageUrl=pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
                +pageUrl+"&action=history"
    print("history url is :"+historyUrl)
    html=urlopen(historyUrl)
    bsObj=BeautifulSoup(bsObj)
    # find only the links with class "mw-anonuserlink" which has ip address instead of usernames
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressLink=set()
    