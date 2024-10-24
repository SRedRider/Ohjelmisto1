class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi siirtyi ylös, nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi siirtyi alas, nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero+1} kerrokseen {kohdekerros}:")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virhe: Hissin numero on virheellinen.")


if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 7)
    talo.aja_hissia(2, 3)
    talo.aja_hissia(0, 1)
