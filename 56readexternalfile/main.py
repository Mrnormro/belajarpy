## membaca file eksternal
print("membaca file txt")
file = open("data.txt","r")

print(f"status read : {file.readable()}")
print(f"status read : {file.writable()}")

# print(file.read())

# print(file.readline(),end="")
# print(file.readline(),end="")

# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

## teknik membuka file
with open("data.txt","r") as file:
    content = file.read()
    print(content)
print(f"apakah file sudah diclose : {file.closed}")