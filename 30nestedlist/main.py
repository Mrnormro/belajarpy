data_0 = [1,2]
data_1 = [3,4]
list_2d = [data_0,data_1,5,6]
print(list_2d)

# contoh
peserta_0 = ["ucup",25,"makan"]
peserta_1 = ["otong",22,"olahraga"]
peserta_2 = ["diki",24,"minum"]
list_peserta = [peserta_0,peserta_1,peserta_2]
print(list_peserta)

for peserta in list_peserta:
    print(f"nama: {peserta[0]}")
    print(f"umur: {peserta[1]}")
    print(f"hobi: {peserta[2]}")
    print()

# dengan reference
list_copy = list_peserta.copy()
print(list_copy)
peserta_0[0] = "michael"
print(list_peserta)
print(list_copy)