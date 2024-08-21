# Kysytään käyttäjältä leiviskät, naulat ja luodit
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


kokonaisgrammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000

print(f"Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
