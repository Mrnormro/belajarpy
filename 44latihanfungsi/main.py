import os

def head():
    os.system('cls')

def inputan():
    panjang = int(input("masukkan panjang : "))
    lebar = int(input("masukkan lebar : "))
    return panjang,lebar

def hitungluas(panjang,lebar):
    L = panjang * lebar
    return L

while True:
    head()
    panjang,lebar = inputan()
    luas = hitungluas(panjang,lebar)
    print("luas =",luas)

    lanjut = input("lanjut atau tidak?(y/n)")
    if lanjut=="n":
        break