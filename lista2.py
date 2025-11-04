import random
l = []

for i in range(50):
    l.append(random.randint(0,50))

l.sort()
print(l)

keresett = int(input("keresett szám : | "))
hányszor=0
if keresett in l:
    hányszor=l.count(keresett)
    print(f"{hányszor} - darab ilyen szám szerepel a listában")
else:
    print("nem szerepel az elem a listában")

while keresett in l:
    l.remove(keresett)

print(l)