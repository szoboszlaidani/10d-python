import random
def gen(list_range=[0,100],db=int(100))->list:return [random.randint(list_range[0],list_range[1]) for _ in range(db)]
with open("fajlkezeles/randomok2.txt","w") as write_to:print(*gen([0,5000],600000),file=write_to)