def sumOfDig(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = abs(int(input("Natural number: ")))
while n > 9:
    n = sumOfDig(n)
print(n)