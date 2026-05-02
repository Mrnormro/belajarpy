nama_global = "otong" # vairabel global

# akses variabel global dalam fungsi

def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam fungsi
for i in range(0,3):
    print(f"loop {i} menampilkan {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel local

def fungsi2():
    nama_local = "ucup"

fungsi2()

# contoh 1 penggunaan akses variabel
def sapatong():
    print(f"hello {nama}")
nama = "otong"
sapatong()

# contoh 2 merubah variabel global
angka = 0

def ubah_angka(nilai_baru):
    global angka # dapatkan akses
    angka = nilai_baru

print(f"sebelum {angka}")
ubah_angka(10)
print(f"sesudah {angka}")

# contoh 3
angka = 0

for i in range(0,5):
    angka+=i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)