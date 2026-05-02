def fungsi(nama,tinggi,berat):
    print(f"{nama},{tinggi},{berat}")

fungsi("ucup",170,50)

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']

    print(f"{nama},{tinggi},{berat}")

fungsi(nama='ucup',tinggi=170,berat=50)

# studi kasus

def math(*args,**kwargs):
    output = 0
    if kwargs['option']=="tambah":
        for angka in args:
            output+=angka
    elif kwargs['option']=="kali":
        output = 1
        for angka in args:
            output*=angka
    else:
        print("opsi tidak ditemukan")
    return output

hasil = math(1,2,3,4,5,6,option="tambah")
print(hasil)
hasil = math(1,2,3,4,5,6,option="kali")
print(hasil)