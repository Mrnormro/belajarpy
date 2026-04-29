#kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

#kumpulan data string
data_string = ["ucup","otong","poris"]
print(data_string)

#kumpulan data boolean
data_boolean = [True,False,False]
print(data_boolean)

#kumpulan data campuran
data_campuran = [1,"ucup",True,2,"otong",False]
print(data_campuran)

# cara alt membuat list
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop, list comprehension
list_for = [i for i in range(0,10)]
print(list_for)

# membuat list menggunakan for if
list_for_if = [i for i in range(0,10) if i%2==0]
print(list_for_if)