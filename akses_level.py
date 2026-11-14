class Siswa:
    def __init__(self, nama, kelas, nis):
        self.nama = nama
        self._kelas = kelas
        self.__nis = nis


s = Siswa("Latifah", "XI RPL", "12345")
print(s.nama)
print(s._kelas)
try:
    print(s.__nis)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")
