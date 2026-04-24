print(5*"=","|KALKULATOR SEDERHANA|",5*"=")
a = float(input("masukkan nilai a : "))
b = float(input("masukkan nilai b : "))
print("operasi (+,-,*,/,%)")
operasi = input("masukkan operasi : ")

if operasi=='+':
    hasil = a + b
    print("hasil operasi =",hasil)
elif operasi=='-':
    hasil = a - b
    print("hasil operasi =",hasil)
elif operasi=='*':
    hasil = a * b
    print("hasil operasi =",hasil)
elif operasi=='/':
    hasil = a / b
    print("hasil operasi =",hasil)
elif operasi=='%':
    hasil = a % b
    print("hasil operasi =",hasil)
else:
    print("operasi tidak diketahui")