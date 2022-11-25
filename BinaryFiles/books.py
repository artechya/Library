import pickle

def CREATE():
    with open('books.dat', 'wb') as f:
        while input("Add a book? (y/n) ").lower() == 'y':
            bcode = input("Book code: ")
            title = input("Title: ")
            sub = input("Subject: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            pickle.dump([bcode, title, sub, qty, price], f)

def DISPLAY():
    print("BCode\tTitle\tSubject\tQuantity\tPrice")
    f = open('books.dat', 'rb')
    while True:
        try:
            rec = pickle.load(f)
            for element in rec:
                print(element, end='\t')
            print()
        except EOFError:
            break
    f.close()

CREATE()
DISPLAY()
