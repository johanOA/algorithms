#https://www.geeksforgeeks.org/python-program-for-merge-sort/
# Python program for implementation of MergeSort
import time
import numpy as np
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.mergeSort(0, len(self.data) - 1)  

    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # Crear arreglos temporales
        L = [0] * n1
        R = [0] * n2

        # Copiar datos a los arreglos temporales L[] y R[]
        for i in range(n1):
            L[i] = self.data[l + i]

        for j in range(n2):
            R[j] = self.data[m + 1 + j]

        # Mezclar los arreglos temporales de nuevo en data[l..r]
        i = 0  # Índice inicial del primer subarreglo
        j = 0  # Índice inicial del segundo subarreglo
        k = l  # Índice inicial del subarreglo mezclado

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.data[k] = L[i]
                i += 1
            else:
                self.data[k] = R[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de L[], si los hay
        while i < n1:
            self.data[k] = L[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de R[], si los hay
        while j < n2:
            self.data[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, l, r):
        if l < r:
            m = l + (r - l) // 2

            # Ordenar las dos mitades
            self.mergeSort(l, m)
            self.mergeSort(m + 1, r)
            self.merge(l, m, r)
