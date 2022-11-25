l1 = int(input("Limit 1: "))
l2 = int(input("Limit 2: "))

if l1 > l2:
    l1, l2 = l2, l1

s = 0
for i in range(l1, l2 + 1):
    print(i, end=' ')
    s += i

print("\nSum =", s)