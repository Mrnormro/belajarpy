# contoh generic
nama = "moren"
str = f"hello  {nama}"
print(str)

#angka
angka = 2009.5
str = f"angka = {angka}"
print(str)

# boolean
bool = True
str = f"boolean : {bool}"
print(str)

# bilangan bulat
angka = 20
str = f"angka = {angka:d}"
print(str)

# bilangan ribuan
angka = 2000
str = f"angka = {angka:,}"
print(str)

# bilangan desimal
angka = 2009.5121
str = f"angka = {angka:.2f}"
print(str)

# menamplkan leading zero
angka = 2009.5121
str = f"angka = {angka:09.2f}"
print(str)

# menampilkan + -
angkamin = -10
angkaplus = 10
format_angkamin = f"minus = {angkamin:+d}"
format_angkaplus = f"minus = {angkaplus:+d}"
print(format_angkamin)
print(format_angkaplus)

# memformat persen
persen = 0.95
format_persen = f"persen = {persen:.0%}"
print(format_persen)

# format angka lain

desimal = 255
binary = f"binary = {bin(desimal)}"
octal = f"octal = {oct(desimal)}"
hex = f"hex = {hex(desimal)}"
print(binary)
print(octal)
print(hex)