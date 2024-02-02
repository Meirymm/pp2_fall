#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def fah_to_cen(f):
    return  (5.0/9.0) * (f - 32)
fahrenheit=86
centigrade=fah_to_cen(fahrenheit)
print(centigrade)
