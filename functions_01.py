#Ejercicio 4: Categorizar edades
#Pide al usuario que introduzca una edad y la clasifique en:
#Bebé (0-2 años)
#Niño (3-12 años)
#Adolescente (13-17 años)
#Adulto (18-64 años)
#Adulto mayor (65 años o más)

edad = int(input("Introduce tu edad: "))

def detector_de_edad(edad):
    
    if edad <= 2:
        print("Bebé")
        
    elif edad >= 3 and edad <= 12:
        print("Niño")
    elif edad >= 13 and edad <= 17:
        print("Adolescente")
    elif edad >= 18 and edad <= 64:
        print("Adulto")
    elif edad >= 65:
        print("Anciano")
        
        
detector_de_edad(edad)

detector_de_edad(4)

detector_de_edad(14)

detector_de_edad(21)

detector_de_edad(67)




# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30


lista = [10,20,30,40,50]

centro = int((len(lista) / 2))


def extractor(lista):
    
    print(lista[centro])
    
    
extractor(lista)



--------------------------------------------------------------

#Ejercicio 2: Combinar y limpiar listas
#Crea dos listas:
#lista_a = [1, 2, 3]
#lista_b = [4, 5, 6, 1, 2]
#Extiende lista_a con lista_b usando extend().
#Elimina la primera aparición del número 1 en lista_a usando remove().
#pasar dos parametros lista y numero a eliminar
#Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
#Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]


def extender(lista_a):
    lista_a.extend(lista_b)
    print(lista_a)
    
extender(lista_a)

eliminator = int(input("introduce el indice: "))
def remover(lista_a, eliminator):
    lista_a.remove(eliminator)
    print(lista_a)
    
remover(lista_a,eliminator)

def popper(lista_a,eliminator):
    element = lista_a.pop(eliminator)
    print(lista_a)
    
popper(lista_a,eliminator)

def clearer(lista_b):
    lista_b.clear()
    print(lista_b)
    
clearer(lista_b)