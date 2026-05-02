def fkuadrat(angka):
    return angka**2

print(fkuadrat(3))

# dengan lambda
kuadrat = lambda angka:angka**2
print(kuadrat(3))

pangkat = lambda num,pow: num**pow
print(pangkat(10,2))

# kegunaan
# sorting untuk list
data_list = ["otong","ucup","dudung"]
data_list.sort()
print(data_list)

# sorting pakai panjang
data_list.sort(key=len)
print(data_list)

# sort pakai lambda
data_list = ["otong","ucup","dudung"]
data_list.sort(key=lambda nama:len(nama))
print(data_list)

#filter
data_angka = [1,2,3,4,5,6,7,8,9]
def kurang_dari_lima(angka):
    return angka<5

# data_angka_new = list(filter(kurang_dari_lima,data_angka))
data_angka_new = list(filter(lambda angka:angka<5,data_angka))
print(data_angka_new)
# genap
data_angka_new = list(filter(lambda angka:angka%2==0,data_angka))
print(data_angka_new)
#ganjil
data_angka_new = list(filter(lambda angka:angka%2!=0,data_angka))
print(data_angka_new)

# anonymous function
# currying <- haskell curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(data_hasil)

# dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(pangkat2(5))
print(pangkat(2)(2))