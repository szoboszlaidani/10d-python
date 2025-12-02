import random
print(*[random.randint(0,5000) for _ in range(1000000)],file=open("fajlkezeles/rovid.txt","w"))