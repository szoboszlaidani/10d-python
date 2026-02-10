import random
numlist=[]
for _ in range(1000):
    numlist.append(random.randint(1,50000))

with open("orai/exportszam.txt","w",) as datafile:
    print(*numlist,sep=";",file=datafile)













print([int(x) for x in open("orai/exportszam.txt","r").read().split(";")])