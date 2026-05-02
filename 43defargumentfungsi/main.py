def sapa(nama = "bro"):
    print("halo",nama)

sapa("ucup")
sapa()

def sapa2(nama,pesan = "apa kabar ?"):
    print(f"hai {nama}, {pesan}")

sapa2("ucup","jangan bolos sekolah")
sapa2("otong")

def pangkat(a,b):
    return a**b

print(pangkat(2,2))