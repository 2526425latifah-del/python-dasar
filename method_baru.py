class Hewan:
    def __init__(self, nama):
        self.nama = nama


class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")


burung = Burung("Kiki")
burung.suara()
burung.terbang()
