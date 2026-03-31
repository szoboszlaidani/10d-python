import csv
from modul import szemely

szemelyek=[]

with open("szemelyek/szemelyek_bov.csv","r",encoding="UTF-8") as datastream:
    next(datastream)
    reader = csv.DictReader(datastream)
    for n in reader:
        szemelyek.append(szemely(*n.values()))

for n in szemelyek:
    print(n)