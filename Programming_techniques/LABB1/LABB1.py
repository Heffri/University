# LABB 1
# Sebastijan Babic
# 2024 - 15 - 01


# tempkonverterings fråga

temperaturkonvertering_val = input("Typer av temperaturkonvertering: \n 1. Fahrenheit -> Celsius \n 2. Celsius -> Fahrenheit \n 3. Kelvin -> Celsius \n 4. Celsius -> Kelvin \n 5. Kelvin - Fahrenheit \n 6. Fahrenheit -> Kelvin \nVilken konvertering vill du göra? Svara med till exempel '1' \n ")

val = int(temperaturkonvertering_val)


# fahr to cels 
if val==1:
    def fahrenheit_to_celsius(t):
        t_celsius = (t - 32) * 5/9
        return t_celsius
    
    svar = input('Ange en temperatur i Fahrenheit: ')
    t_fahrenheit = float(svar)
    t = fahrenheit_to_celsius(t_fahrenheit)
    print("Celsius: ", t)




# cels to fahr
elif val==2:
    def celsius_to_fahrenheit(t):
        t_fahrenheit = (t * 9/5) + 32
        return t_fahrenheit
    
    svar = input("Ange en temperatur i Celsius: ")
    t_celsius = float(svar)
    t = celsius_to_fahrenheit(t_celsius)
    print("Fahrenheit: ", t)




# kelv to cels
elif val==3:
    def kelvin_to_celsius(t): 
        t_kelvin = t - 273.15
        return t_kelvin
    
    svar = input("Ange en temperatur i Kelvin: ")
    t_kelvin = float(svar)
    t = kelvin_to_celsius(t_kelvin)
    print("Celsius: ", t)





# cels to kelv
elif val==4:
    def celsius_to_kelvin(t): 
        t_celsius = t + 273.15
        return t_celsius
    
    svar = input("Ange en temperatur i Celsius: ")
    t_celsius = float(svar)
    t = celsius_to_kelvin(t_celsius)
    print("Kelvin: ", t)




# kelv to fahr
elif val==5:
    def kelvin_to_fahrenheit(t): 
       t_fahrenheit = t * 9/5 - 459.67
       return t_fahrenheit
    
    svar = input("Ange en temperatur i Kelvin: ")
    t_fahrenheit = float(svar)
    t = kelvin_to_fahrenheit(t_fahrenheit)
    print("Fahrenheit: ", t)




# fahr to kelv 
elif val==6:
    def fahrenheit_to_kelvin(t): 
       t_kelvin = (t + 459.67) * 5/9
       return t_kelvin
    
    svar = input("Ange en temperatur i Fahrenheit: ")
    t_kelvin = float(svar)
    t = fahrenheit_to_kelvin(t_kelvin)
    print("Kelvin: ", t)



