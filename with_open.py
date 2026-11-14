with open("jurnal.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

with open("jurnal.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

with open("jurnal.txt", "r") as file:
    for baris in file:
        print(baris.strip())
