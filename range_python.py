# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")


for nums in range(1,11):
    print(nums)



# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().


for nums in range(1,21,2):
    print(nums)


# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().


 for nums in range(5,51):
    if nums % 5 == 0:
        print(nums)


# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")


numbers = []

for num in range(1,11):
    numbers.append(num)
    

numbers.reverse()
print(numbers)


# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().


suma = 0

for nums in range(1,101):
    suma = nums + suma
    print(suma)
        
#print(suma)


# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

Lo que estaba mal:


number = input("introduce un numero: \n")
tabla = 0


for num in range(10):
     
    print(f"{number} x {num} = {num} ")

---------------------------------------------------


number = int(input("introduce un numero: \n"))
tabla = 0




for num in range(1,11):
    tabla = number * num
    print(f"{number} x {num} = {tabla}")



