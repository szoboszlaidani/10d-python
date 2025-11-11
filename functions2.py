import random, math


def hatvany(alap:int, kitevo:int) -> int:
    return alap**kitevo

def hatvany2(alap:int, kitevo:int) -> int:
    return math.pow(alap,kitevo)


szamok=[random.randint(1,100),random.randint(1,100)]

print(f"eredmény: {hatvany(szamok[0],szamok[1])}")
print(f"eredmény: {hatvany2(szamok[0],szamok[1])}")