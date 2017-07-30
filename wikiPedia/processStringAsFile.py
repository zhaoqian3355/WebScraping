from urllib.request import urlopen
from io import StringIO
import csv

response=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")
data=response.read().decode('ascii','ignore')
dataFile=StringIO(data)
csvReader=csv.reader(dataFile)

for row in csvReader:
    print(row)

dataFile.seek(0)
dictReader=csv.DictReader(dataFile)


for row in dictReader:
    print(row)
