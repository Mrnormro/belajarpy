# 1. menyambung string (concatenate)
nama_awal = "ucup"
nama_akhir = "surucup"
nama_lengkap = nama_awal + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator
# cek apakah ada char atau string di string
d = "d"
status = d in nama_lengkap
print(status)

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-0-3 : " + nama_lengkap[0:3])

# item paling kecil dan besar
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))


ascii_code = ord(" ")
print("ascii spasi : " + str(ascii_code))
ascii_code = ord("u")
print("ascii u : " + str(ascii_code))
data = 117
print("char 117 : " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong perkontong"
jumlah = data.count("o")
print(jumlah)