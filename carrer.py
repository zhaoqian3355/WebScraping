from urllib.request import urlopen
import requests
import json
import math

data={
    "Year":2017,
    "Month":8
}

headers={
    "Host":"career.dlut.edu.cn",
    "Origin":"http://career.dlut.edu.cn",
    "Referer":"http://career.dlut.edu.cn/dgjyw/jsp/Portal/frCalendar/Cal.html",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
}

r = requests.post('http://career.dlut.edu.cn/dgjyw/jsp/CalendarEvent.jsp', data,headers=headers)
url="http://career.dlut.edu.cn/dgjyw/jsp/Portal/News/NewsDtl/ZC17090137/ZC17090137.html?Stamp=1505321040493"
text=r.text.split("\b")[1:-1]
result=[]
pageCount=math.ceil(len(text)//3)
for item in range(0,pageCount):
    result.append(text[item*3:(item+1)*3])
print(result)