from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import pymssql

conn=pymssql.connect('127.0.0.1', 'sa', '123456', "Ctrip")

def saveCity():
    cursor=conn.cursor(as_dict=True)
    try:
        with open("ctrip/city.json","rb+") as city:
            cityDic=json.loads(city.read().decode())
            allCity=[]
            for key in cityDic:
                for subKey in cityDic[key]:
                    for  cityInfo in cityDic[key][subKey]:
                        dataArr=cityInfo["data"].split("|")
                        item=[cityInfo["display"],cityInfo["data"]]
                        for subData in dataArr:
                            item.append(subData)
                        item.append(key)
                        item.append(subKey)
                        print(item)
                        allCity.append(tuple(item))
            cursor.executemany("""INSERT INTO [dbo].[City] VALUES(%s, %s, %s, %s, %d, %s,%s, %s)""",allCity)
            conn.commit()
    except Exception as ex:
        print("Save Failed:{0}".format(ex))

# saveCity()

def insertDpcApc():
    try:

        cursor=conn.cursor(as_dict=True)
        cursor.execute("Select * from city")
        cityCode=[]
        dpcApc=[]
        for row in cursor:
            cityCode.append(row["Code"])
        for dpc in cityCode:
            for apc in cityCode:
                item=[]
                if dpc!=apc:
                    item.append(dpc)
                    item.append(apc)
                    item.append(0)
                    item.append(0)
                    dpcApc.append(tuple(item))
        cursor.executemany("""INSERT INTO [dbo].[DpcApc] VALUES(%s, %s, %d, %d)""",dpcApc)
        conn.commit()
        print("save successfully!")
    except Exception as ex:
        print(ex)
        
# insertDpcApc()

# fightUrl='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=DLC&ACity1=SHA&SearchType=S&DDate1=2016-11-05&IsNearAirportRecommond=0&rk=0.8936676051200609145454&CK=052284128A811F5580F548DF4AE52C1E&r=0.53111172658318670744115'
# fightUrl='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=DLC&ACity1=SHA&SearchType=S&DDate1=2017-04-02&IsNearAirportRecommond=0&LogToken=924dfa5aae9845ec87bc84f4ed6914cc&rk=7.7963247727761775154223&CK=47F7898F2B1C006CD6E977FD32FBFADD&r=0.4625425849728326452313'
fightUrl="http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=BJS&ACity1=SHA&SearchType=S&DDate1=2017-05-20"
response=urlopen(fightUrl)
byteData=response.read()
stringData=byteData.decode('gb2312')
print(stringData)
# x=json.loads(stringData)

# lips=x["lips"]