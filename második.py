szám_1=int(input("Kérem az első számot: "))
szám_2=int(input("Kérem a második  számot: "))
szám_3=int(input("Kérem a harmadik számot: "))
szám_4=int(input("Kérem a negyedik  számot: "))

szorzat = szám_1*szám_2*szám_3*szám_4
hányados = szám_1/szám_2/szám_3/szám_4
maradék = szám_1%szám_2%szám_3%szám_4

print(f"Szorzat: {szorzat}\nHányados:{hányados:.2f}\nMaradék: {maradék}")