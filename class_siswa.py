class Siswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")


s1 = Siswa("Latifah", "RPL")
s2 = Siswa("Rani", "Akuntansi")
s1.sapa()
s2.sapa()
