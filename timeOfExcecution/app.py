#pip install matplotlib
#pip install setuptools
#python3 -m venv myenv
#deactivate
import time
import matplotlib.pyplot as plt
from bubbleSort import BubbleSort
from quicksort import QuickSort
from pigeonholeSort import PigeonholeSort
from mergeSort import MergeSort
from bitonic_sort import BitonicSort

class SortExecution:
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
        method_to_call()  # Llama al método
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convertir a milisegundos
        self.timeOfExecution.append((sort_algorithm.__class__.__name__, execution_time))
        return execution_time

if __name__ == "__main__":
    execution = SortExecution()
    n = execution.load_numbers('numbers_matrix.txt')

    # Crear copias de la lista original para cada algoritmo
    original_numbers = execution.numbers.copy()

    # BubbleSort
    #bubble_sorter = BubbleSort(original_numbers.copy())  # Crear instancia de BubbleSort
    #execution_time = execution.record_time(bubble_sorter, 'sort')  # Llama al método sort
    #print(f"Tiempo de ejecución BubbleSort: {execution_time:.2f} ms")

    # QuickSort
    quick_sort = QuickSort(original_numbers.copy())  # Pasa el arreglo al constructor
    execution_time = execution.record_time(quick_sort, 'sort')
    print(f"Tiempo de ejecución QuickSort: {execution_time:.2f} ms")

    # Crear instancia de la clase PigeonholeSort
    pigeonhole_sorter = PigeonholeSort(original_numbers.copy())
    execution_time = execution.record_time(pigeonhole_sorter, 'pigeonhole_sort')
    print(f"Tiempo de ejecución pigeonholeSort: {execution_time:.2f} ms")

    # Crear instancia de la clase MergeSort
    merge_sorter = MergeSort(original_numbers.copy())
    execution_time = execution.record_time(merge_sorter, 'sort')
    #print(f"Lista ordenada (primeros 100 elementos): {merge_sorter.data[:100]}")
    print(f"Tiempo de ejecución MergeSort: {execution_time:.2f} ms")

    # BitonicSort
    bitonic_sorter = BitonicSort(original_numbers.copy())  # Crear instancia de BitonicSort
    execution_time = execution.record_time(bitonic_sorter, 'sort')  # Llama al método sort
    print(f"Tiempo de ejecución BitonicSort: {execution_time:.2f} ms")

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
    plt.ylabel('Tiempo (ms)')

    plt.show()
