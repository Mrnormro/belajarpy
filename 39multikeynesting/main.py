import datetime

mahasiswa1 = {
    'nama':'ucup surucup',
    'nim':'1922222',
    'sks':144,
    'beasiswa':False,
    'lahir':datetime.datetime(2003,2,10)
}
mahasiswa2 = {
    'nama':'otong surotong',
    'nim':'1921111',
    'sks':140,
    'beasiswa':False,
    'lahir':datetime.datetime(2004,3,12)
}
mahasiswa3 = {
    'nama':'dadang suradang',
    'nim':'1923333',
    'sks':123,
    'beasiswa':True,
    'lahir':datetime.datetime(2003,4,2)
}

data_mahasiswa = {
    'M001':mahasiswa1,
    'M002':mahasiswa2,
    'M003':mahasiswa3
}

print(f"{'M001':<6} {"nama":<17} {"SKS":<3} {"Beasiswa":<9} {"lahir":<10}")
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")
