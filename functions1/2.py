#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9 )*(fahrenheit - 32)
    return celsius

#example
fahrenheit = float (100)
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius) 
