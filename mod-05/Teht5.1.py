import random

arpakuutioiden_lukumaara = int(input("Kuinka monta arpakuutiota haluat heittää? "))

summa = 0

for i in range(arpakuutioiden_lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto

print("Silmälukujen summa on:", summa)
