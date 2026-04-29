a = ["otong","ucup","dudung"]
print(a)

b = a
print(b)

# member a dirubah
a[1] = "michael"
b.sort()
print(a)
print(b)

# address
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# duplikat list dengan copy
c = a.copy()
print(a)
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")
print(f"address a = {hex(id(c))}")

c[1] = "dadang"
print(a)
print(b)
print(c)
