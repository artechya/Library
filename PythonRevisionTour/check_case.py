c = input("Enter a character: ")

if c:
    c = c[0]
    if c.isupper():
        print("Upper case")
    elif c.islower():
        print("Lower case")
    elif c.isdigit():
        print("Digit")
    elif c.isspace():
        print("Space")
    else:
        print("Special character")
else:
    print("Empty string")