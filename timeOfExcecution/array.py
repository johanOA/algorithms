import random

# Generar 10 mil números de 8 dígitos
numbers = [random.randint(10000000, 99999999) for _ in range(10000)]

# Mezclar los números para que estén desordenados
random.shuffle(numbers)

# Mostrar los primeros 10 números como ejemplo
print(numbers[:10])

