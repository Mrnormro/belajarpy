# merubah case dari string
# merubah semua ke upper case
halo = "halo"
print(halo)
halo = halo.upper()
print(halo)

# merubah semua ke lower case
sapa = "SAPA"
print(sapa)
sapa = sapa.lower()
print(sapa)

# pengecekan dengan isX method
# contoh pengecekan lower case dan upper case
salam = "sist"
apakah_lower = salam.islower()
print(salam, "is lower : ", apakah_lower)
apakah_upper = salam.isupper()
print(salam, "is lower : ", apakah_upper)

# isalpha() untuk mengecek semuanya huruf
# islnum() untuk mengecek semuanya huruf dan angka
# isdecimal() angka saja
# isspace() spasi,tab,newline \n
# istitle() semua kata dimulai huruf kapital

judul = "Narnia Last War"
cek_judul = judul.istitle()
print(cek_judul)

# cek kompenen startswith() endswith()
cek_start = "Narnia".startswith("Nar")
print(cek_start)

# penggabungan komponen join() split()
pisah = ["a","k","u"]
gabung = "".join(pisah)
print(pisah)
print(gabung)
gabungan = "aku capek"
pisahan = gabungan.split(" ")
print(pisahan)
print(gabungan)

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"=")
print("'"+tengah+"'")
#menghilangkan
tengah = tengah.strip("=")
print("'"+tengah+"'")