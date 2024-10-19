#https://www.geeksforgeeks.org/bitonic-sort/
import time
import numpy as np
# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
class BitonicSort:
    def __init__(self, data):
        self.data = data

    def compAndSwap(self, i, j, dire):
        if (dire == 1 and self.data[i] > self.data[j]) or (dire == 0 and self.data[i] < self.data[j]):
            self.data[i], self.data[j] = self.data[j], self.data[i]

    def bitonicMerge(self, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                self.compAndSwap(i, i + k, dire)
            self.bitonicMerge(low, k, dire)
            self.bitonicMerge(low + k, k, dire)

    def bitonicSort(self, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            self.bitonicSort(low, k, 1)       # Sort in ascending order
            self.bitonicSort(low + k, k, 0)   # Sort in descending order
            self.bitonicMerge(low, cnt, dire)

    def sort(self):
        self.bitonicSort(0, len(self.data), 1)  # Sort in ascending order
