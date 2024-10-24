import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            # Arvotaan nopeuden muutos väliltä -10 km/h ja +15 km/h
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            # Liikutetaan autoa yhden tunnin ajan
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailun '{self.nimi}' tilanne:")
        print(f"{'Rekisteritunnus':<15}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}{'Huippunopeus (km/h)':<20}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15}{auto.nopeus:<15}{auto.kuljettu_matka:<20}{auto.huippunopeus:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


if __name__ == "__main__":
    # Luodaan lista autoista (10 kpl)
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus 100-200 km/h väliltä
        autot.append(Auto(rekisteritunnus, huippunopeus))

    # Luodaan kilpailu
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    # Kilpailu jatkuu, kunnes jokin auto on saavuttanut 8000 km
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        # Tulostetaan tilanne joka kymmenes tunti
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    # Kilpailun lopullinen tilanne
    print(f"\nKilpailu on päättynyt {tunti} tunnin jälkeen.")
    kilpailu.tulosta_tilanne()
