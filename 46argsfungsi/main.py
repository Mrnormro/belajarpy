# *args

def fungsi(nama,tinggi,berat):
    print(f"{nama},{tinggi},{berat}")

fungsi("ucup",180,67)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama},{tinggi},{berat}")

fungsi(["otong",100,100])

# *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama},{tinggi},{berat}")

fungsi('dudung',120,40)

# studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output+=angka
    return output

print(tambah(1,2,3,4,5,6,7,8,9))