from Helpers.formatters import Table

name = input("Employee name: ")
bsal = float(input("Enter basic salary: "))
ta = 0.7 * bsal
da = 0.4 * bsal
hra = 0.25 * bsal
gross = bsal + ta + da + hra

table = Table([[name, bsal, ta, da, hra, gross]], ['Name', 'Basic Salary', 'Transport Allowance', 'Domestic Allowance', 'Human Resource Allowance', 'Gross Salary'])
table.display()