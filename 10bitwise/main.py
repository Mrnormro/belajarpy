a = 9 #00001001
b = 5 #00000101

# bitwise or |
print("OPERATOR OR=========(|)")
c = a | b
print("nilai :",a,"biner :",format(a,"08b"))
print("nilai :",b,"biner :",format(b,"08b"))
print("-----------------------------------(|)")
print("nilai :",c,"biner :",format(c,"08b"))
print()

# bitwise and &
print("OPERATOR AND=========(&)")
c = a & b
print("nilai :",a,"biner :",format(a,"08b"))
print("nilai :",b,"biner :",format(b,"08b"))
print("-----------------------------------(&)")
print("nilai :",c,"biner :",format(c,"08b"))
print()

# bitwise xor ^
print("OPERATOR XOR=========(^)")
c = a ^ b
print("nilai :",a,"biner :",format(a,"08b"))
print("nilai :",b,"biner :",format(b,"08b"))
print("-----------------------------------(^)")
print("nilai :",c,"biner :",format(c,"08b"))
print()

# bitwise not ~
print("OPERATOR NOT=========(~)")
c = ~a
print("nilai :",a,"biner :",format(a,"08b"))
print("-----------------------------------(~)")
print("nilai :",c,"biner :",format(c,"08b"))
print()

# bitwise shift right >>
print("OPERATOR shift right=========(>>)")
c = a >> 1
print("nilai :",a,"biner :",format(a,"08b"))
print("-----------------------------------(>>)")
print("nilai :",c,"biner :",format(c,"08b"))
print()

# bitwise shift left <<
print("OPERATOR shift left=========(<<)")
c = a << 1
print("nilai :",a,"biner :",format(a,"08b"))
print("-----------------------------------(<<)")
print("nilai :",c,"biner :",format(c,"08b"))