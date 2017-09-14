from urllib.request import urlopen
import requests
import json
import math
import pandas as pd

data={
    "Year":2017,
    "Month":9
}

headers={
    "Host":"career.dlut.edu.cn",
    "Origin":"http://career.dlut.edu.cn",
    "Referer":"http://career.dlut.edu.cn/dgjyw/jsp/Portal/frCalendar/Cal.html",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
}

r = requests.post('http://career.dlut.edu.cn/dgjyw/jsp/CalendarEvent.jsp', data,headers=headers)
url="http://career.dlut.edu.cn/dgjyw/jsp/Portal/News/NewsDtl/{0}/{1}.html"
text=r.text.split("\b")[1:-1]
result=[]
pageCount=math.ceil(len(text)//3)
for item in range(0,pageCount):
    result.append(text[item*3:(item+1)*3])
df=pd.DataFrame(result,columns=["Date","Name","Code"])
# df["Url"]=url.format(df["Code"],df["Code"])
df.to_excel("company.xlsx",index=False)
print(df)