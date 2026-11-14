class Siswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")


class SiswaBaru(Siswa):
    def __init__(self, nama, jurusan, kelas):
        super().__init__(nama, jurusan)
        self.kelas = kelas

    def info(self):
        super().info()
        print(f"Kelas: {self.kelas}")


baru = SiswaBaru("Latifah", "RPL", "XI RPL")
baru.info()
