## operasi
data =["ucup","otong","dudung"]

# mengambil data dari list
print(data[0])

# mengambil info jumlah data dalam list
print(len((data)))

## manipulasi data list
# menambahkan item pada list sesuai posisi
print(data)
data.insert(1,"kentung")
print(data)

# menambah di akhir list
data.append("jajang")
print(data)

# menambah list dengan list
data_baru = ["ujang","kibo","hayam"]
data.extend(data_baru)
print(data)

# merubah data
data[2] = "michael"
print(data)

# remove data
data.remove("ujang")
print(data)

# remove data palng belakang
data.pop()
print(data)