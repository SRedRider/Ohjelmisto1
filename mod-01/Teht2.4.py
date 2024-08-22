# Kysytään käyttäjältä kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

# Lasketaan lukujen summa
summa = luku1 + luku2 + luku3

# Lasketaan lukujen tulo
tulo = luku1 * luku2 * luku3

# Lasketaan lukujen keskiarvo
keskiarvo = int(summa / 3)


print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo:.2f}")
