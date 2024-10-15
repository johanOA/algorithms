def sumArray(arr, i):
    if i >= len(arr) - 1:
        return arr[i]
    
    return arr[i] + sumArray(arr, i+1)

def main():
    a = [1,2,3,5,6]
    print(sumArray(a, 0))

if __name__ == "__main__":
    main()