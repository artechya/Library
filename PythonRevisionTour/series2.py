l = abs(int(input("Limit: ")))
s = 0

for i in range(1, l + 1):
    s += i * (i + 1) / 2 / (2 * i - 1)

print(s)