import random
import time

# https://ellibrodepython.com/bubble-sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: 
            break

# Generar 10 mil números de 8 dígitos
numbers = [random.randint(10000000, 99999999) for _ in range(100000)]

# Mezclar los números para que estén desordenados
random.shuffle(numbers)

# Mostrar los primeros 100 números como ejemplo, desordenados
print(numbers[:100])

print("-------------------------------------------------------------------------------------")

# Medir el tiempo de ejecución
start_time = time.time()  # Tiempo inicial
bubble_sort(numbers)
end_time = time.time()    # Tiempo final

# Mostrar la lista ordenada, solo los primeros 100
print(numbers[:100])  

# Mostrar el tiempo en milisegundos
execution_time = (end_time - start_time)  # Convertir a milisegundos
print(f"Tiempo de ejecución: {execution_time:.2f} sg")
