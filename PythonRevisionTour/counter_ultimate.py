def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def reverseNum(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r

def isAdam(n):
    rev = reverseNum(n)
    if rev ** 2 == reverseNum(n ** 2):
        return True
    else:
        return False

def isPerfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    
    if s == n:
        return True
    else:
        return False

l1 = abs(int(input("Natural no. Limit 1: ")))
l2 = abs(int(input("Natural no. Limit 2: ")))
if l1 > l2:
    l1, l2 = l2, l1

cPr = cPe = cAd = 0
for i in range(l1 + 1, l2):
    if isPrime(i):
        cPr += 1
    if isPerfect(i):
        cPe += 1
    if isAdam(i):
        cAd += 1

print(f"{cPr} prime numbers, {cPe} perfect numbers, {cAd} adam numbers")