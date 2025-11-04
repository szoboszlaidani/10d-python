import random,time,os
l=[]
for i in range(10):
    l.append([])
    for _ in range(10):
        l[i].append(random.randint(0,1))
for _ in range(100): 
    time.sleep(.1)
    os.system("cls")
    for i in l:
        print(str(i).replace("0"," ").replace("1","#"))