def isPrime(n, i):
    
    if n <= 1:
        return True    
    if i == 1:
        return True 

    if n%i == 0:
        return False

    return isPrime(n, i-1)
    
def countPrimes(arr, count, i):

    if i >= len(arr):
        return count
    
    if isPrime(arr[i], arr[i] - 1):
        count = count + 1
    
    return countPrimes(arr, count, i+1)

def main():
    a = [1,2,3,4,5,6,7,8,9]
    print(countPrimes(a, 0, 0))

if __name__ == "__main__":
    main()