# pass > tidak dieksekusi
angka = 0
while angka < 5:
    angka+=1
    if angka == 3:
        pass
    print(angka)

# continue > tidak mengeksekusi kode selanjutnya dan melanjutkan loop
angka = 0
while angka < 5:
    angka+=1
    print(angka)
    if angka == 3:
        continue
    print("yo")