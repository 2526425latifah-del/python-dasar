from abc import ABC, abstractmethod


class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass


class Tunai(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} dengan uang tunai")


class Transfer(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} lewat transfer bank")


def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)


proses_pembayaran(Tunai(), 25000)
proses_pembayaran(Transfer(), 60000)
