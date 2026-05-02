# fungsi dengan argument

def sapa(nama):
    print("halo", nama)

sapa("ucup")

def tambah(a,b):
    hasil = a + b
    print(hasil)

tambah(10,5)

data_siswa = ["ucup","otong","dadang"]

def absen(list_siswa):
    nama_siswa = list_siswa.copy()
    for siswa in nama_siswa:
        print("halo",siswa)

absen(data_siswa)