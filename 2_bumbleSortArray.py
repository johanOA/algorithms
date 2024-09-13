def sortArray(arr, i, j):
    
    if i >= len(arr) -1:
        return arr
    
    if j >= len(arr) - i - 1:
        return sortArray(arr, i+1, 0)
    
    
    if arr[j] < arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
    return sortArray(arr, i, j+1)


def main():
    a = [1,2,23,4,5,1]
    a = sortArray(a, 0, 0)
    for elemento in a:
        print(elemento)

if __name__ == "__main__":
    main() 