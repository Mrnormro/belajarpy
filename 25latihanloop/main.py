tinggi = 5
for i in range(1,tinggi+1):
    print("*"*i)

for i in range(1,tinggi+1):
    print((tinggi-i+1)*"*")

for i in range(1,tinggi+1):
    print((tinggi-i)*" "+i*"*")

for i in range(1,tinggi+1):
    print((i-1)*" "+(tinggi-i+1)*"*")

for i in range(1,tinggi+1):
    print((tinggi-i)*" "+(i*2-1)*"*")
