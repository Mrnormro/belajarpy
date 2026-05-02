# operator dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dunf':'dudung surudung'
}

# panjang dict
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# cek key ada atau tidak
KEY = 'cup'
CHECHKKEY = KEY in data_dict
print(f"apapkah {KEY} ada di data dict : {CHECHKKEY}")

# mengakses value
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis','gaada cuy'))

# update data
data_dict['cup'] = "ucup siganteng"
print(data_dict)
data_dict['sep'] = "asep sikasep"
print(data_dict)

data_dict.update({'cup':'ucup surucup'})
print(data_dict)
data_dict.update({'cuy':'encuyy'})
print(data_dict)

# delete data
del data_dict['dunf']
print(data_dict)