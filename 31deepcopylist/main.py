data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(data_2d)
print(data_2d_copy)

# mengambil
data = data_2d[0][0]
print(data)

#address
print(f"address data_2d = {hex(id(data_2d))}")
print(f"address data_2d = {hex(id(data_2d_copy))}")

print(f"address data_2d = {hex(id(data_2d[0]))}")
print(f"address data_2d = {hex(id(data_2d_copy[0]))}")
data_2d[1][0] = 5
print(data_2d)
print(data_2d_copy)

# deep copy
from copy import deepcopy

data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"address data_2d = {hex(id(data_2d[0]))}")
print(f"address data_2d = {hex(id(data_2d_deepcopy[0]))}")