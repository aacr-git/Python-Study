"""

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


numero_uno = input("Introcuce el primer numero: ")
numero_dos = input("introduce el segundo numero: ")

if (numero_uno > numero_dos):
    print(f"{numero_uno} es mayor que {numero_dos}")
elif (numero_uno < numero_dos):
    print(f"{numero_dos} es mayor que {numero_uno}")
else :
    print(f"{numero_uno} y {numero_dos} son iguales")








# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)


numero1 = input("dame un numero: \n")

numero2 = input("dame otro numero: \n")

suma = (int(numero1)) + (int(numero2))

print(f"suma es igual a: {suma} \n")

resta = (int(numero1)) - (int(numero2))

print(f"resta es igual a : {resta} \n")

multiplicacion = (int(numero1)) * (int(numero2))

print(f"multiplicacion es igual: {multiplicacion} \n ")

if (numero2 != 0):
    division = (int(numero1)) / (int(numero2))
    print(f"la division es igual: {float(division)}")
else:
    print("no se puede dividir entre 0")







# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.





año = int(input("introduce un año:" ))

if (año % 4 == 0):
    if (año % 100 == 0):
        if (año % 400 == 0):
            print(f"{año} es bisiesto ")
elif (año % 4 == 0) and (año % 100 == 0):
        if (año % 400 != 0):
            print(f"{año} no es bisiesto")
 



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)



edad = int(input("Introduce una edad: \n"))

if (edad <= 2):
    print("Bebé")
    
elif ((edad >= 3) and (edad <= 12)):
    print("Niño")
    
elif ((edad >= 13) and (edad <= 17)):
    print("Adolescente")
    
elif ((edad >= 18) and (edad <= 64)):
    print("Adulto")
    
else: 
    print("Adulto mayor")




"""