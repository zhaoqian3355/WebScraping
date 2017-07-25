from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

downloadDirectory='downloaded'
baseUrl="http://pythonscraping.com"

def getAbsoluteUrl(baseUrl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source[4:]
        url="http://"+source
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path=absoluteUrl.replace("www.","")
    path=path.replace(baseUrl,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html)
downloadList=bsObj.findAll(src=True)

for dowload in downloadList:
    fileUrl=getAbsoluteUrl(baseUrl,dowload["src"])
    if fileUrl is not None:
        print(fileUrl)
    urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))
    