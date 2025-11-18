import random,math,csv

def összeg(a:int, b:int) -> int:
    return a+b

def összeg2(a:int, b:int) -> int:
    össz = a+b
    return össz

def összeg3(a:int,b:int,c = int(100)) -> int:
     print(f"összeg: {a+b+c}")

def összeg4(a:int,b:int,c = int(100),d = int(200)) -> int:
    print(f"összeg: {a+b+c+d}")
     

a,b=[2,4]
print(f"elsö: {összeg(a,b)}\n"
      f"második: {összeg2(a,b)}")
összeg3(a,b)
b = int(input("B számot bitte | "))
a = int(input("A számot bitte | "))
összeg4(a,b)