# loop dict

data_teman = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung'
}

# loop (mengeluarkan key)
for teman in data_teman:
    print(teman)

# operator mengambil item / iterables
keys = data_teman.keys()
print(keys)

for key in data_teman.keys():
    print(data_teman.get(key))

values = data_teman.values()
print(values)

for value in data_teman.values():
    print(value)

items = data_teman.items()
print(items)

for items in data_teman.items():
    print(items)

for key,values in data_teman.items():
    print(f"{key}, {value}")