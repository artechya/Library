s = input("Enter a string: ")
lc = uc = d = sp = spl = 0

for c in s:
    if c.islower():
        lc += 1
    elif c.isupper():
        uc += 1
    elif c.isdigit():
        d += 1
    elif c.isspace():
        sp += 1
    else:
        spl += 1

print(f"There are {lc} lower, {uc} upper, {d} digits, {sp} spaces, {spl} spl characters")
