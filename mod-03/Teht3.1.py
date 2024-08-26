kuhan_pituus = int(input("Anna kuhan pituuden senttimetrinä: "))

if kuhan_pituus < 37:
    kuhan_puuttuva_pituus = 37 - kuhan_pituus
    print(f"Kuha on alamittainen. Laskea kuhan takaisin järveen")
    print(f"Kuha on {kuhan_puuttuva_pituus} cm kokorajoituksen alapuolella")

else:
    print("Kuhan pituus täyttää kokorajoituksen")