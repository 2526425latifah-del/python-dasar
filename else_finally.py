try:
    hasil = 12 / 4
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", hasil)
finally:
    print("Selesai memproses.")
