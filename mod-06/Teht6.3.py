def muunna_litroiksi(gallona):
    return gallona * 3.785


while True:
    gallona = float(input("Anna bensiinin määrä gallonina (negatiivinen lopettaa): "))

    if gallona < 0:
        print("Annoit negatiivinen syöte. Ohjelma lopetettu")
        break


    litra = muunna_litroiksi(gallona)

    print(f"{gallona} gallonaa vastaa {litra:.2f} litraa.")



