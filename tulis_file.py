file = open("catatan.txt", "w")
file.write("Halo, ini catatan Latifah!\n")
file.write("Baris kedua...\n")
file.close()

file = open("catatan.txt", "a")
file.write("Baris tambahan...\n")
file.close()
print("File catatan.txt selesai ditulis")
