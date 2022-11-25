n = abs(int(input("Natural number: ")))

if n != 0:
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    
    if s == n:
        print("Perfect number")
    else:
        print("Not a perfect number")
else:
    print("0 is not a perfect number")