c = input("Enter character: ")

if c and c[0].isalpha():
    if c[0].lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Neither")