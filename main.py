import re
import urllib.request

url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=DLC&ACity1=SHA&SearchType=S&DDate1=2016-09-06';

html=urllib.request.urlopen(url);
pw =html.read()
print(pw);