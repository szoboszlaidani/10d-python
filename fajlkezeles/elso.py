import random
lista = []
for _ in range(1000):
    lista.append(random.randint(0,5000))

with open("fajlkezeles/randomok.txt","w",encoding="utf-8") as write_to:
    print(*lista,sep="\n",file=write_to)
