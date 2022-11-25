n = abs(int(input("Number of rows: ")))

for i in range(n):
    for j in range(i + 1):
        print(chr(j + 97), end=' ')
    print()