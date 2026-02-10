
with open("orai/textil.txt","r",encoding="UTF-8") as forras:
    szoveg = forras.read()

sep= ",.-;>*'%/=()"
for i in list(sep):
    szoveg=szoveg.replace(i,"")
szavak=szoveg.split()

a=[]
for i in szavak:
    if i.startswith("a") and len(i)>2:a.append(i)

print(*a,sep=";",file=open("orai/export.txt","w",encoding="UTF-8"))


with open("orai/export.txt","r",encoding="UTF-8") as forras:
    to_be_sorted = forras.read()

szavak=to_be_sorted.split(";")
len_min_max=["",""]
for x in szavak:
    if len(x)<len(len_min_max[0]) or len(len_min_max[0])==0:len_min_max[0]=x
    if len(x)>len(len_min_max[1]):len_min_max[1]=x

print(*len_min_max)