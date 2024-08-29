luvut = []

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luvut.append(int(syote))


if luvut:
    pienin_luku = min(luvut)
    suurin_luku = max(luvut)
    print("Pienin luku:", pienin_luku)
    print("Suurin luku:", suurin_luku)
else:
    print("Et syöttänyt yhtään lukua.")
