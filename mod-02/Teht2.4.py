# Kysytään käyttäjältä kolme kokonaisluku
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

# Lukujen summa
summa = luku1 + luku2 + luku3

# Lukujen tulo
tulo = luku1 * luku2 * luku3

# Lukujen keskiarvo
keskiarvo = int(summa / 3)


print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo}")
