#konversi satuan temperature

##celcius

# ###celsiuc ke fahrenheit
# celcius = 30
# fahrenheit = 1.8 * celcius + 32
# print(celcius,"c =",fahrenheit,"f")
# ###celsiuc ke kelvin
# celcius = 30
# kelvin = celcius + 273.15
# print(celcius,"c =",kelvin,"k")

# #fahrenheit

# ###fahrenheit ke celcius
# fahrenheit = 130
# celcius = 5 / 9 * (fahrenheit - 32)
# print(fahrenheit,"f =",celcius,"c")
# ###fahrenheit ke kelvin
# fahrenheit = 130
# kelvin = 5 / 9 * (fahrenheit - 32) + 273.15
# print(fahrenheit,"f =",kelvin,"c")

#kelvin

###kelvin ke celcius
kelvin = 130
celcius = kelvin - 273.15
print(kelvin,"k =",celcius,"c")

###kelvin ke fahrenheit
kelvin = 130
fahrenheit = 9 / 5 * (kelvin - 273.15) + 32
print(kelvin,"k =",fahrenheit,"f")