# gabungan area rentang dari angka

angka = int(input("masukkan angka : "))
#+++++++++3-------10++++++
print("kurang dari 3 atau lebih besar dari 10")
hasil = (angka < 3) or (angka > 10)
print(hasil)

#------3+++++++++10------
print("lebih dari 3 dan kurang dari 10")
hasil = (angka > 3) and (angka < 10)
print(hasil)