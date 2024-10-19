class JumpSearch:
    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.n = len(array)

    def search(self):
        return self.jump_search()

    def jump_search(self):
        # Calcular el tamaño del salto
        jump = int(self.n ** 0.5)
        prev = 0

        # Saltar a través de los bloques
        while prev < self.n and self.array[min(jump, self.n) - 1] < self.target:
            prev = jump
            jump += int(self.n ** 0.5)
            if prev >= self.n:
                return -1  # No se encontró el elemento

        # Búsqueda lineal en el bloque encontrado
        for i in range(prev, min(jump, self.n)):
            if self.array[i] == self.target:
                return i  # Retornar el índice donde se encontró el elemento

        return -1  # No se encontró el elemento