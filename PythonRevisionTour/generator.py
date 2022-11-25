n = abs(int(input("Natural number: ")))

if n != 0:
    if n % 2 == 0:
        n -= 1

    for i in range(n, 0, -2):
        print(i)