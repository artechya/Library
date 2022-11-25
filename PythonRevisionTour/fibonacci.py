n_terms = abs(int(input("Number of terms: ")))
a, b = -1, 1

for i in range(n_terms):
    c = a + b
    print(c)
    a, b, = b, c
