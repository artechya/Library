p = float(input("Principal: "))
r = float(input("Rate (in %): "))
n = int(input("Number of years: "))

si = p * n * r / 100
ci = p * (1 + r / 100) ** n - p

print("SI =", si, "CI =", ci)