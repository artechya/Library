def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(10, 100):
    if isPrime(i):
        print(i)