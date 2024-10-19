import time
import os
import sys
import matplotlib.pyplot as plt

from jump_search import JumpSearch

# Obtén la ruta del directorio padre (en este caso, "Analisis de Algoritmos")
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agrega esa ruta al sys.path
sys.path.append(parent_dir)
from binary_search import BinarySearch
from linear_search import LinealSearch
from limited_linear_search import LimitedLinealSearch
from timeOfExcecution.quicksort import QuickSort


class SearchExecution:
    def __init__(self):
        self.timeOfExecution = []
        self.numbers = []

    def load_numbers(self, filename):
        with open('numbers_matrix.txt', 'r') as file:
            for line in file:
                self.numbers.extend(map(int, line.split()))
        return len(self.numbers)

    def record_time(self, sort_algorithm, method_name):
        start_time = time.time()
        method_to_call = getattr(sort_algorithm, method_name)  # Obtiene el método
        result = method_to_call()  # Llama al método
        end_time = time.time()
        execution_time = ((end_time - start_time) * 1000)*1000  # Convertir a milisegundos
        self.timeOfExecution.append((sort_algorithm.__class__.__name__, execution_time))
        return execution_time, result
    
    def record_timeSort(self, sort_algorithm, method_name):
        start_time = time.time()
        method_to_call = getattr(sort_algorithm, method_name)  # Obtiene el método
        method_to_call()  # Llama al método
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convertir a milisegundos
        return execution_time

if __name__ == "__main__":
    execution = SearchExecution()
    n = execution.load_numbers('numbers_matrix.txt')
    target = 94429622
    original_numbers = execution.numbers.copy()

    # Para que este funcione la lista debe estar ordenada
    # QuickSort
    quick_sort = QuickSort(original_numbers)  # Pasa el arreglo al constructor
    execution_time = execution.record_timeSort(quick_sort, 'sort')

    lineal_search = LinealSearch(original_numbers, target)
    execution_time, index = execution.record_time(lineal_search, 'search')
    print(f"Tiempo de ejecución Lineal Search: {execution_time:.2f} µs en posicion: {index}")

    limited_lineal_search = LimitedLinealSearch(original_numbers, target)
    execution_time, index = execution.record_time(limited_lineal_search, 'search')
    print(f"Tiempo de ejecución Limited Lineal Search: {execution_time:.2f} µs en posicion: {index}")


    binary_search = BinarySearch(original_numbers, target)
    execution_time, index = execution.record_time(binary_search, 'search')
    print(f"Tiempo de ejecución Limited BinarySearch: {execution_time:.2f} µs en posicion: {index}")

    jump_search = JumpSearch(original_numbers, target)
    execution_time, index = execution.record_time(jump_search, 'search')
    print(f"Tiempo de ejecución JumpSearch: {execution_time:.2f} µs en posicion: {index}")

    # Crear una lista de tuplas con los nombres y tiempos de ejecución
    names, values = zip(*execution.timeOfExecution)

    # Ordenar las tuplas de mayor a menor según los valores
    sorted_pairs = sorted(zip(values, names), reverse=True)

    # Desempaquetar las listas ordenadas
    sorted_values, sorted_names = zip(*sorted_pairs)

    # Crear el gráfico de barras
    plt.bar(sorted_names, sorted_values)

    # Agrega título y etiquetas
    plt.title('Tiempos de Ejecucion de Algoritmos')
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo (µs)')

    plt.show()