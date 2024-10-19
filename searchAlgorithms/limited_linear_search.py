#https://www.geeksforgeeks.org/python-program-for-linear-search/
class LimitedLinealSearch:
    def __init__(self, arr, objetivo):
        self.arr = arr  
        self.objetivo = objetivo

    def search(self):
        return self.linear_search()

    def linear_search(self):
        for i in range(len(self.arr)):
            if self.arr[i] == self.objetivo:
                return i
        return -1