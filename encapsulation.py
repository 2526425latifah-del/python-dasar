class Tabungan:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


akun = Tabungan(5000)
print("Saldo awal:", akun.lihat_saldo())
akun.setor(1500)
print("Setelah setor:", akun.lihat_saldo())
akun.tarik(2000)
print("Setelah tarik:", akun.lihat_saldo())
akun.tarik(99999)
