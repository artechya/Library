import math

x = float(input("Float: "))
n = abs(int(input("Limit: ")))
s = 0

for i in range(1, n + 1):
    s += x ** i / math.factorial(i) * (-1) ** (i + 1)

print(s)