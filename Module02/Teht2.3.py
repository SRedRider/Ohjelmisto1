# Kysytään käyttäjältä suorakulmion kanta ja korkeus
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Lasketaan suorakulmion piiri (P = 2 * (kanta + korkeus))
piiri = 2 * (kanta + korkeus)

# Lasketaan suorakulmion pinta-ala (A = kanta * korkeus)
pinta_ala = kanta * korkeus


print(f"Suorakulmion piiri on: {piiri}")
print(f"Suorakulmion pinta-ala on: {pinta_ala}")
