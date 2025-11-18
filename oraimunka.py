import random
lista=[random.randint(1,99) for _ in range(100)]

lista.sort() # sortolja a listát
lista.pop(1) # kiszedi az első elemet
lista.append(1) # hozzáad 1 et a lista elejéhez
lista.reverse() # megtükrözi a listát
lista.remove(1) # kiszedi az összes 1-est

for x in lista:
    print(x) # for ciklusos bejárás
print(lista)