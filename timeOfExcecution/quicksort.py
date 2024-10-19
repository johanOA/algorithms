# https://www.geeksforgeeks.org/python-program-for-quicksort/

# Función para encontrar la posición de la partición
import random
import time

class QuickSort:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    def sort(self):
            self.quick_sort(0, len(self.arreglo) - 1)

    def quick_sort(self, bajo, alto):
        if bajo < alto:
            pi = self.particion(bajo, alto)
            self.quick_sort(bajo, pi - 1)
            self.quick_sort(pi + 1, alto)

    def particion(self, bajo, alto):
        pivote = self.arreglo[alto]
        i = bajo - 1

        for j in range(bajo, alto):
            if self.arreglo[j] <= pivote:
                i += 1
                self.arreglo[i], self.arreglo[j] = self.arreglo[j], self.arreglo[i]

        self.arreglo[i + 1], self.arreglo[alto] = self.arreglo[alto], self.arreglo[i + 1]
        return i + 1