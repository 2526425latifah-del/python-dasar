class Bebek:
    def suara(self):
        return "Kwek"


class Sapi:
    def suara(self):
        return "Moo"


def cetak_suara(hewan):
    print(hewan.suara())


cetak_suara(Bebek())
cetak_suara(Sapi())
