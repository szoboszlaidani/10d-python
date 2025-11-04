import random
l=[]
for x in range(5):l.append(random.randint(1,7))
if int(input("kérek egy számot: | ")) in l:print("nagyon jó")