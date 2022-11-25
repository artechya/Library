n = float(input("Float: "))
print("Integer part: ", int(n))
print("Decimal part: ", round(n - int(n), len(str(n).partition('.')[2])))
