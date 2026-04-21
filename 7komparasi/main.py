# hasil operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 10

# lebih besar dari >
hasil = a > 3
print(a,">",3,"=",hasil)

# lebih kecil dari <
hasil = a < 3
print(a,"<",3,"=",hasil)

# lebih besar atau sama dengan >=
hasil = a >= 4
print(a,">=",4,"=",hasil)

# lebih kecil atau sama dengan <=
hasil = a <= 4
print(a,"<=",4,"=",hasil)

# sama dengan ==
hasil = b == 4
print(b,"==",4,"=",hasil)

# tidak sama dengan ==
hasil = b == 4
print(b,"==",4,"=",hasil)

# tidak sama dengan !=
hasil = b != 4
print(b,"!=",4,"=",hasil)

# is untuk komparasi object identity
hasil = a is b
print(hasil)

# is not
hasil = a is not b
print(hasil)