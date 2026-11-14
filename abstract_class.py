from abc import ABC, abstractmethod


class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass


class Bebek(Hewan):
    def suara(self):
        return "Kwek"


class Sapi(Hewan):
    def suara(self):
        return "Moo"


b = Bebek()
s = Sapi()
print(b.suara())
print(s.suara())
try:
    h = Hewan()
except TypeError:
    print("Class abstract tidak bisa dibuat objeknya")
