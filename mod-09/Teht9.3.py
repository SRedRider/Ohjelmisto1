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
        print(f"Auto kulki {kuljettu} km {tuntia} tunnin aikana.")
        print(f"Kuljettu matka on nyt {self.kuljettu_matka} km.")


if __name__ == "__main__":
    auto = Auto("ABC-123", 142)

    auto.kiihdyta(60)
    print(f"Auton nopeus on nyt: {auto.nopeus} km/h")

    auto.kuljettu_matka = 2000
    print(f"Kuljettu matka alussa: {auto.kuljettu_matka} km")

    auto.kulje(1.5)
