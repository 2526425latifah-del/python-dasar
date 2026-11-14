file = open("catatan.txt", "r")
print(file.read())
file.close()

file = open("catatan.txt", "r")
for baris in file:
    print(baris.strip())
file.close()
