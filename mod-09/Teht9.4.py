import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntia):
        kuljettu = self.nopeus * tuntia
        self.kuljettu_matka += kuljettu



if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        rekisteritunnus = f"ABC-{i}"
        autot.append(Auto(rekisteritunnus, huippunopeus))

    # Kilpailun simulaatio
    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)

            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False
                break

    print(f"{'Rekisteri':<10} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
    print("=" * 65)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20.1f}")
