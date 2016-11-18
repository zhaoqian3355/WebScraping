from os import getenv
import pymssql
import datetime
import json

conn = pymssql.connect(host='10.0.0.157', user='sa', password='123456', database='Test')
cursor = conn.cursor()
with open('train_list.json',encoding='utf-8') as data_file:    
    data = json.load(data_file)

for dtKey in data:
    dtData=data[dtKey]
    for typeKey in dtData:
        typeData=dtData[typeKey]
        for train in typeData:
            cursor.execute("INSERT INTO Train VALUES ('"+train["station_train_code"]+"', '"+train["train_no"]+"','"+dtKey+"','"+typeKey+"')")

# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()