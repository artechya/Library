n = abs(int(input("Natural number: ")))

def reverseNum(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r

rev = reverseNum(n)
if rev ** 2 == reverseNum(n ** 2):
    print("Adam number")
else:
    print("Not an adam number")
