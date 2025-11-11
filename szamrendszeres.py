import random
lista,szamrendszer,pl,db = [],10,[7,2,1],0
for _ in range(1000):lista.append(round(random.randint(0,szamrendszer-1)))
for x in range(len(lista)-len(pl)):
    da=True
    for lenght in range(len(pl)):
        if not lista[x+(lenght-1)]==pl[lenght-1]:da=False
    if da:db+=1
print(f"ennyiszer szerepel a {str(pl).replace(", ","")} : {db}")