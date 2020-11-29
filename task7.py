def celcius_to_fahrenheit(temp):
    fr = (temp/5)*9 + 32
    return fr
    

def fahrenheit_to_celsius(temp):
    c = (temp-32)*5 / 9
    return c


print(fahrenheit_to_celsius(33))
print(celcius_to_fahrenheit(0.5555555556))
