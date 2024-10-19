class LinealSearch:
    def __init__(self, arr, objetivo):
        self.arr = arr  
        self.objetivo = objetivo

    def search(self):
        return self.linear_search()

    def linear_search(self):
        aux = 0
        for i in range(len(self.arr)):
            if self.arr[i] == self.objetivo:
                aux = i
        return aux
