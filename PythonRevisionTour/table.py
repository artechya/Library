n = int(input("Integer: "))
l = abs(int(input("Table limit: ")))

if l != 0:
    for i in range(1, l + 1):
        print(n, '*', i, '=', n*i)