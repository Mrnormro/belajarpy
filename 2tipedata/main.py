# a = 10, adalah variabel dengan nilai 20

# integer
data_int = 1
print("data : ",data_int)
print("bertipe :",type(data_int))

# float
data_float = 3.14
print("data : ",data_float)
print("bertipe :",type(data_float))

# string
data_string = "moreno"
print("data : ",data_string)
print("bertipe :",type(data_string))

# bool
data_bool = True
print("data : ",data_bool)
print("bertipe :",type(data_bool))

# bilangan kompleks
data_complex = complex(5,6)
print("data : ",data_complex)
print("bertipe :",type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ",data_c_double)
print("bertipe :",type(data_c_double))