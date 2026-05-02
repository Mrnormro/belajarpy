# __main__

# pada file program utama
print(f"nilai __name__ pada main.py : {__name__}")

# pada file program eksternal
import fungsi

## contoh penggunaan __main__

#deklarasi
def fungsi_tambah(a,b):
    return a+b

#fungsi uatama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(hasil)

## import package
import package