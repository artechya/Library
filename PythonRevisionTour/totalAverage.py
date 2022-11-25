from Helpers.formatters import Table

name = input("Name: ")
print("Enter marks in: ")
m = float(input("Maths: "))
p = float(input("Physics: "))
c = float(input("Chemistry: "))
e = float(input("English: "))
cs = float(input("CSC: "))

total = m + p + c + cs + e
average = total / 5

table = Table([[name, m, p, c, e, cs, total, average]], ['Name', 'Maths', 'Physics', 'Chem', 'English', 'CS', 'Total', 'Average'])
table.display()