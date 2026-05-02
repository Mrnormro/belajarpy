# copy dict
data_teman = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung'
}

friends = data_teman.copy()
print(data_teman)
print(friends)

data_teman['cup']='ucup keren'
print(data_teman)
print(friends)

# pop dictionary
data_ucup = friends.pop('cup')
print(data_ucup)
print(friends)

# popitem dict
dataakhir = friends.popitem()
print(dataakhir)
print(friends)