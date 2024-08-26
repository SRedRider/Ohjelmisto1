# Kysytään käyttäjältä suorakulmion kanta ja korkeus
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Suorakulmion piiri (P = 2 * (kanta + korkeus))
piiri = 2 * (kanta + korkeus)

# Suorakulmion pinta-ala (A = kanta * korkeus)
pinta_ala = kanta * korkeus


print(f"Suorakulmion piiri on: {piiri}")
print(f"Suorakulmion pinta-ala on: {pinta_ala}")
