import random


kolmenumeroinen_koodi = ""
for i in range(3):
    kolmenumeroinen_koodi += str(random.randint(0, 9))

nelinumeroinen_koodi = ""
for i in range(4):
    nelinumeroinen_koodi += str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroinen_koodi}")
