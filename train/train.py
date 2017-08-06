import pandas as pd
from urllib.request import urlopen
from datetime import date,datetime

today=str(date.today())

def getTrainInfo(date):
    df = pd.read_json("train_list.json")
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


dfTrain = getTrainInfo()


def getStationInfo():
    with open("station_name.txt") as f:
        stations = f.read()
    stations=stations[:-2]
    stations=stations.split('@')
    stations=stations[1:]
    station_names = list(map(lambda x: x.split('|'), stations))
    df = pd.DataFrame(station_names, columns=[
                      'pingyin_abbr', 'station_name', 'station_code', 'pingyin', 'pingyin_short', 'station_num'])

    return df


dfStation = getStationInfo()


result=pd.merge(left=dfTrain,right=dfStation,how='left',left_on='from_station',right_on='station_name')
result=result.rename(columns={'station_code':'from_station_telecode'})
result=result.rename(columns={'station_name':'from_station_name'})
result=result.loc[:,['station_train_code', 'train_no', 'train_type', 'train_code',
        'from_station','from_station_name', 'to_station', 
        'from_station_telecode']]

result=pd.merge(left=result,right=dfStation,how='left',left_on='to_station',right_on='station_name')
result=result.rename(columns={'station_code':'to_station_telecode'})
result=result.rename(columns={'station_name':'to_station_name'})
result=result.loc[:,['station_train_code', 'train_no', 'train_type', 'train_code',
        'from_station','from_station_name', 'to_station','to_station_name',
        'from_station_telecode','to_station_telecode']]
result.to_excel("search.xlsx")

def getTrainStation(train_no,from_station,to_station,date):
    # https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=240000K6810U&from_station_telecode=BJP&to_station_telecode=DLT&depart_date=2017-08-06
    data=urlopen("https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={0}&from_station_telecode={1}&to_station_telecode={2}&depart_date={3}".format(train_no,from_station,to_station,str(date))