sukupuoli = input("Anna biologisen sukupuoli: ")


sukupuoli = sukupuoli.lower()



if sukupuoli == "nainen" or sukupuoli == "mies":
    if sukupuoli == "nainen":
        hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo (g/l): "))
        if hemoglobiiniarvo < 117:
            print("Sinun hemoglobiiniarvo on alhainen")
        elif hemoglobiiniarvo > 175:
            print("Sinun hemoglobiiniarvo on korkea")
        elif hemoglobiiniarvo > 117 and hemoglobiiniarvo < 175:
            print("Sinun hemoglobiiniarvo on normaali")



    if sukupuoli == "mies":
        hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo (g/l): "))
        if hemoglobiiniarvo < 134:
            print("Sinun hemoglobiiniarvo on alhainen")
        elif hemoglobiiniarvo > 195:
            print("Sinun hemoglobiiniarvo on korkea")
        elif hemoglobiiniarvo > 134 and hemoglobiiniarvo < 195:
            print("Sinun hemoglobiiniarvo on normaali")

else:
    print("Syötevirhe")







