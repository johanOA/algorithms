import math
import numpy as np
import random

# Generar 10 mil números de 8 dígitos
numbers = np.random.randint(10000000, 99999999, size=10000000)

# Mezclar los números para que estén desordenados
random.shuffle(numbers)

n = int(math.sqrt(len(numbers)))+2

# Guarda todos los datos a un txt
with open('numbers_matrix.txt', 'w') as file:
    for i in range(n):
        # Escribir una fila de n números
        row = numbers[i*n:(i+1)*n]
        file.write(' '.join(map(str, row)) + '\n')

# Mostrar los primeros 10 números como ejemplo
print(numbers[:10])