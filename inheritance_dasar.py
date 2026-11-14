class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")


class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")


class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")


kucing = Kucing("Mimi")
anjing = Anjing("Bobi")
kucing.suara()
anjing.suara()
