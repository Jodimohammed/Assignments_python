#python program that Convert a list of Celsius temperatures to Fahrenheit.

celsius_list = [40 , 30 , 2 , 15]

fahrenheit_list = []

for deg in celsius_list:
    fah_deg = deg * 9/5 + 32
    
    fahrenheit_list.append(fah_deg)
    
print(fahrenheit_list)