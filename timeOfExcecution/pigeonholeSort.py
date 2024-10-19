#https://www.geeksforgeeks.org/python-program-for-pigeonhole-sort/
import time
import numpy as np

# Python program to implement Pigeonhole Sort  
class PigeonholeSort:
    def __init__(self, data):
        self.data = data

    def pigeonhole_sort(self): 
        # size of range of values in the list 
        my_min = int(np.min(self.data))  # Convert to int
        my_max = int(np.max(self.data))  # Convert to int
        size = my_max - my_min + 1
    
        # our list of pigeonholes 
        holes = [0] * size 

        # Populate the pigeonholes. 
        for x in self.data: 
            assert np.issubdtype(type(x), np.integer), "integers only please"  # Cambia aquí
    
            holes[x - my_min] += 1
    
        # Put the elements back into the array in order. 
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                self.data[i] = count + my_min 
                i += 1