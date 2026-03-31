import csv
from modul import data as dv

data=[]

with open("gyak/data.csv","r",encoding="UTF-8") as datastream:
    next(datastream)
    reader = csv.DictReader(datastream)
    for n in reader:
        data.append(dv(n.values()))

for n in data:
    print(n)