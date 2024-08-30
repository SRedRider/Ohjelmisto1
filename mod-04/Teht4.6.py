import random


pisteiden_maara = int(input("Kuinka monta pistettä arvotaan? "))


ympyrassa = 0

for i in range(pisteiden_maara):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x * x + y * y < 1:
        ympyrassa += 1

pi_likiarvo = 4 * ympyrassa / pisteiden_maara

print("Piin likiarvo on:", pi_likiarvo)
