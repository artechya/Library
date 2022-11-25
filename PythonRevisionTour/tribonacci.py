n = abs(int(input("Number of terms: ")))

a, b, c = -1, 1, 0

for i in range(n):
    d = a + b + c
    print(d)
    a, b, c = b, c, d
    
