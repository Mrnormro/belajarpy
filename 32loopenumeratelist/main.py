# loop dari list

# for loop
list_angka = [4,3,4,2,1]

for angka in list_angka:
    print(angka)

peserta = ["ucup","dudung","otong"]

for nama in peserta:
    print(peserta)

jumlah = len(list_angka)

for i in range(jumlah):
    print(list_angka[i])

#list comprehension
data_list = ["ucup",1,2,3,"orong"]
[print(i) for i in data_list]

# enumerate
for index,data in enumerate(data_list):
    print(f"index ke-{index}, data = {data}")