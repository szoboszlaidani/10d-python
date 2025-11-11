import random, math


lista = []
for _ in range(1000):
    lista.append(round(random.random()))

db=0
for x in range(len(lista)-2):
    if lista[x] == 1 and lista[x+1] == 1 and lista[x+2] == 1:
        db+=1

print(f"ennyiszer van binárisban a 7: {db}")

def hatvany(alap:int, kitevo:int) -> int:
    return alap**kitevo

def hatvany2(alap:int, kitevo:int) -> int:
    return math.pow(alap,kitevo)


szamok=[random.randint(1,100),random.randint(1,100)]

print(f"eredmény: {hatvany(szamok[0],szamok[1])}")
print(f"eredmény: {hatvany2(szamok[0],szamok[1])}")