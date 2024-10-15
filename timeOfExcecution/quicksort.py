# https://www.geeksforgeeks.org/python-program-for-quicksort/

# Función para encontrar la posición de la partición
import random
import time


def particion(arreglo, bajo, alto):
    
    # Elegir el elemento más a la derecha como pivote
    pivote = arreglo[alto]

    # Puntero para el elemento mayor
    i = bajo - 1

    # Recorrer todos los elementos
    # Comparar cada elemento con el pivote
    for j in range(bajo, alto):
        if arreglo[j] <= pivote:

            # Si se encuentra un elemento menor que el pivote
            # intercambiarlo con el elemento mayor apuntado por i
            i = i + 1

            # Intercambiando el elemento en i con el elemento en j
            (arreglo[i], arreglo[j]) = (arreglo[j], arreglo[i])

    # Intercambiar el elemento pivote con el elemento mayor especificado por i
    (arreglo[i + 1], arreglo[alto]) = (arreglo[alto], arreglo[i + 1])

    # Devolver la posición desde donde se ha realizado la partición
    return i + 1

# Función para realizar quicksort
def quickSort(arreglo, bajo, alto):
    if bajo < alto:

        # Encontrar el elemento pivote de tal manera que
        # los elementos menores que el pivote estén a la izquierda
        # los elementos mayores que el pivote estén a la derecha
        pi = particion(arreglo, bajo, alto)

        # Llamada recursiva en la izquierda del pivote
        quickSort(arreglo, bajo, pi - 1)

        # Llamada recursiva en la derecha del pivote
        quickSort(arreglo, pi + 1, alto)


# Generar 10 mil números de 8 dígitos
numbers = [random.randint(10000000, 99999999) for _ in range(1000000)]

# Mezclar los números para que estén desordenados
random.shuffle(numbers)

# Mostrar los primeros 100 números como ejemplo, desordenados
print(numbers[:100])

print("-------------------------------------------------------------------------------------")

# Medir el tiempo de ejecución
start_time = time.time()  # Tiempo inicial
quickSort(numbers, 0, len(numbers)-1)
end_time = time.time()    # Tiempo final

# Mostrar la lista ordenada, solo los primeros 100
print(numbers[:100])  

# Mostrar el tiempo en milisegundos
execution_time = (end_time - start_time) * 1000 # Convertir a milisegundos
print(f"Tiempo de ejecución: {execution_time:.2f} ms")
