class Tabungan:
    def __init__(self, saldo):
        self.__saldo = saldo

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah


akun = Tabungan(2000)
akun.setor(750)
print("Saldo:", akun.lihat_saldo())
