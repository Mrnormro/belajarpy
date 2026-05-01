# program list
list_buku = []
while True:
    print("tambah datab buku")
    judul = input("masukkan judul : ")
    penulis = input("masukkan penulis : ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("JUDUL\tPENULIS")
    for buku in list_buku:
        print(f"{buku[0]}\t{buku[1]}")