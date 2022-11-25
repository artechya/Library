def isArmstrong(n):
    nDig = len(str(n))
    s = 0

    c = n
    while c > 0:
        dig = c % 10
        s += dig ** nDig
        c //= 10

    if s == n:
        return True
    else:
        return False

l1 = abs(int(input("Limit 1: ")))
l2 = abs(int(input("Limit 2: ")))
if l1 > l2:
    l1, l2 = l2, l1

i = l1 + 1
while i < l2:
    if isArmstrong(i):
        print(i)
    i += 1