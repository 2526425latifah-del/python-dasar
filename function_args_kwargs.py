def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)


jumlahkan(2, 4, 6, 8)


def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


biodata(nama="Latifah", kelas="XI RPL", kota="Subang")
