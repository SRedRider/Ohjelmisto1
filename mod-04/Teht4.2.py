while True:
    tuuma = int(input("Anna tuuma: "))
    if tuuma < 0:
        break
    print (f"{tuuma} tuuma senttimetreiksi on {tuuma * 2.54}cm")

print("Annoit negatiivisen tuumamäärän. Ohjelma lopetettu")

