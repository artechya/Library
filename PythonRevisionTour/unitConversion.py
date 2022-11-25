m = float(input("Enter distance in metres: "))
cm = m * 100
i = cm / 2.54
f = i / 12

print("Distance in cm: ", cm)
print("Distance in inches: ", round(i, 2))
print("Distance in feet: ", round(f, 2))