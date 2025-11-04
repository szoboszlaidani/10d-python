import random
játékos_1= random.randint(1,6)
játékos_2= random.randint(1,6)

if játékos_1>játékos_2:
    print("játékos 1 nyert")
elif játékos_1<játékos_2:
    print("játékos 2 nyert")
else:
    print("döntetlen")

print(f"{játékos_1}|{játékos_2}")