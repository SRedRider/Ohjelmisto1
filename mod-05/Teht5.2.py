luvut = []


while True:
    syote = input("Anna luku (tai jätä tyhjäksi lopettaaksesi): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:", luvut[:5])
