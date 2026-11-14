class Hewan:
    def suara(self):
        return "Hewan bersuara"


class Bebek(Hewan):
    def suara(self):
        return "Kwek"


class Sapi(Hewan):
    def suara(self):
        return "Moo"


daftar_hewan = [Bebek(), Sapi(), Hewan()]
for h in daftar_hewan:
    print(h.suara())
