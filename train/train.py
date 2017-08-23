import pandas as pd
from urllib.request import urlopen
from datetime import date, datetime
from pymongo import MongoClient
import json
from urllib.request import Request
import ssl
from sqlalchemy import create_engine
import numpy as np

today = str(datetime(2017, 8, 23))
mongoClient = MongoClient("mongodb://localhost:27017")
trainData = mongoClient.TrainData
train = trainData.Train

engine = create_engine('mssql+pymssql://sa:!QAZxsw2@zhaoqian3355:1433/Ctrip')

def getTrainInfo(date):
    df = pd.read_json("train_list.js",encoding="utf-8")
    df1 = df[str(date)]
    dfList = []
    for item in df1.index:
        dfItem = pd.DataFrame(df1[item])
        dfItem['train_type'] = item
        dfList.append(dfItem)
    result = pd.concat(dfList)
    result = result.reset_index(drop=True)
    result["train_code"] = ''
    result["from_station"] = ''
    result['to_station'] = ''
    for i in range(0, len(result)):
        stationCode = result.station_train_code[i]
        result["train_code"][i] = stationCode[0:stationCode.index("(")]
        result["from_station"][i] = stationCode[stationCode.index(
            "(") + 1:stationCode.index("-")]
        result["to_station"][i] = stationCode[stationCode.index(
            "-") + 1:stationCode.index(")")]
    return result


def getStationInfo():
    with open("station_name.txt",encoding="utf-8") as f:
        stations = f.read()
    stations = stations[:-2]
    stations = stations.split('@')
    stations = stations[1:]
    station_names = list(map(lambda x: x.split('|'), stations))
    df = pd.DataFrame(station_names, columns=[
                      'pingyin_abbr', 'station_name', 'station_code', 'pingyin', 'pingyin_short', 'station_num'])

    return df


# dfTrain = getTrainInfo(today)
# dfStation = getStationInfo()

# result = pd.merge(left=dfTrain, right=dfStation, how='left',left_on='from_station', right_on='station_name')
# result = result.rename(columns={'station_code': 'from_station_telecode'})
# result = result.rename(columns={'station_name': 'from_station_name'})
# result = result.loc[:, ['station_train_code', 'train_no', 'train_type', 'train_code',
#                         'from_station', 'from_station_name', 'to_station',
#                         'from_station_telecode']]

# result = pd.merge(left=result, right=dfStation, how='left',
#                   left_on='to_station', right_on='station_name')
# result = result.rename(columns={'station_code': 'to_station_telecode'})
# result = result.rename(columns={'station_name': 'to_station_name'})
# result = result.loc[:, ['station_train_code', 'train_no', 'train_type', 'train_code',
#                         'from_station', 'from_station_name', 'to_station', 'to_station_name',
#                         'from_station_telecode', 'to_station_telecode']]
# result.index=np.arange(1,len(result)+1)
# result.index.name="Id"
# result["IsSelect"]=0
# result.to_excel("train.xlsx")

df = pd.read_excel("./train.xlsx")


def getTrainStation(train_no, from_station, to_station, date):
    try:
        context = ssl._create_unverified_context()
        req = Request("https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={0}&from_station_telecode={1}&to_station_telecode={2}&depart_date={3}".format(
            '11000C100102', 'CCT', 'YXL', '2017-08-10'))
        data = urlopen(req, context=context)
        data = json.loads(data.read().decode())
        print(data)
    except Exception as ex:
        print(ex)


# for index, row in df.iterrows():
#     print(index)
#     print(row.from_station_telecode)
#     print(row.to_station_telecode)
#     print(row.train_no)
#     getTrainStation(row.train_no,row.from_station_telecode,row.to_station_telecode,today)

df.to_sql("Train", engine, if_exists="replace",index=False)