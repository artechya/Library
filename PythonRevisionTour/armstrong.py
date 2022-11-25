n = abs(int(input("Enter a natural number: ")))

nDig = len(str(n))
s = 0

c = n
while c > 0:
    dig = c % 10
    s += dig ** nDig
    c //= 10

if s == n:
    print("Armstrong number")
else:
    print("Not an armstrong number")