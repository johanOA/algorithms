def esPotencia(n, b):
    if n==1:
        return True
    if b==n:
        return True
    if b==0 or b<1 or b==1:
        return False
    else:
        return esPotencia(n, b**0.5)
    
def main():
    n=5
    b=25
    f = esPotencia(n, b)
    print(f)

if __name__ == "__main__":
    main()