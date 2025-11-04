import random

lista = []

for _ in range(500): 
    lista.append(random.randint(0,500))


print(f"lista {lista}\n"
      f"első {lista[0]}\n"
      f"utolsó {lista[-1]}\n"
      f"első 5 {lista[:5]}")