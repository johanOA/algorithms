# https://www.geeksforgeeks.org/python-program-for-stooge-sort/

import random
import time


def stoogesort(arr, l, h): 
 if l >= h: 
  return
 
 # If first element is smaller 
 # than last,swap them 
 if arr[l]>arr[h]: 
  t = arr[l] 
  arr[l] = arr[h] 
  arr[h] = t 
 
 # If there are more than 2 elements in 
 # the array 
 if h-l+1 > 2: 
  t = (int)((h-l+1)/3) 
 
  # Recursively sort first 2/3 elements 
  stoogesort(arr, l, (h-t)) 
 
  # Recursively sort last 2/3 elements 
  stoogesort(arr, l+t, (h)) 
 
  # Recursively sort first 2/3 elements 
  # again to confirm 
  stoogesort(arr, l, (h-t)) 
'''
# Generar 10 mil números de 8 dígitos
numbers = [random.randint(10000000, 99999999) for _ in range(10000)]

# Mezclar los números para que estén desordenados
random.shuffle(numbers)

# Mostrar los primeros 100 números como ejemplo, desordenados
print(numbers[:100])

print("-------------------------------------------------------------------------------------")

# Medir el tiempo de ejecución
start_time = time.time()  # Tiempo inicial
stoogesort(numbers, 0, len(numbers)-1)
end_time = time.time()    # Tiempo final

# Mostrar la lista ordenada, solo los primeros 100
print(numbers[:100])  

# Mostrar el tiempo en milisegundos
execution_time = (end_time - start_time) * 1000 # Convertir a milisegundos
print(f"Tiempo de ejecución: {execution_time:.2f} ms")
'''