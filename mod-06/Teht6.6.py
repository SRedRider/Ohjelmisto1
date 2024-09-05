import math

def laske_yksikkohinta(halk_cm, hinta_eur):
    # Lasketaan pizzan säde
    sade_m = (halk_cm / 2) / 100  # Muutetaan säde metreiksi
    # Lasketaan pizzan pinta-ala (A = pi * r^2)
    pinta_ala = math.pi * (sade_m ** 2)
    # Lasketaan yksikköhinta
    yksikkohinta = hinta_eur / pinta_ala
    return yksikkohinta

halk1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

halk2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

yksikkohinta1 = laske_yksikkohinta(halk1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halk2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} euroa/m²")
print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} euroa/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")
