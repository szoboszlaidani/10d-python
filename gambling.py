import random
history,pénz,d=[[],1,3]
for _ in range(200):
    for _ in range(d):
        dobás=random.randint(1,6)
        if dobás<=4:pénz-=1;
        elif dobás<=5:pénz+=1;
        else:pénz+=3
    history.append(pénz)
for i in history:print(" "*(50-int(max(0,-i)))+"█"*int(i)+"+"*-int(i)+f"| {i}$")