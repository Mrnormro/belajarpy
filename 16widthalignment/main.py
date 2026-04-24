data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 170.5
data_uk_sepatu = 43

# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, no sepatu = {data_uk_sepatu}"
print(5*"=","biodata",5*"=")
print(data_string)

#string multiline
data_string = f"nama = {data_nama}\numur = {data_umur}\ntinggi = {data_tinggi}\nno sepatu = {data_uk_sepatu}"
print(5*"=","biodata",5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
"""
print(5*"=","biodata",5*"=")
print(data_string)