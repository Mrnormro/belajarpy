# 1. mode write
# akan membuat file baru jika tidak ada,
# dan akan overwrite isinya

with open("data.txt","w",encoding="utf-8") as file:
    file.write("ucup")
with open("data.txt","w",encoding="utf-8") as file:
    file.write("ketimpa")

# 2. mode append
with open("data2.txt","w",encoding="utf-8") as file:
    file.write("ucup\n")

with open("data2.txt","a",encoding="utf-8") as file:
    file.write("ucup2")

# 3. mode r+

with open("data3.txt","w") as file:
    file.write("data 3")


with open("data3.txt","r+") as file:
    file.write("tambah pake r+1\n")
    file.write("tambah pake r+2\n")

with open("data3.txt","r+") as file:
    data = file.read()
    print(data)

with open("data3.txt","r+") as file:
    file.write("tambah pake r+3\n")
