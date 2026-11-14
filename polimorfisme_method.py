class Bebek:
    def suara(self):
        return "Kwek"


class Sapi:
    def suara(self):
        return "Moo"


hewan = [Bebek(), Sapi()]
for h in hewan:
    print(h.suara())
