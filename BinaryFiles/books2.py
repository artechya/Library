import pickle

def APPEND():
    with open('books.dat', 'ab') as f:
        while input("Add a book? (y/n) ").lower() == 'y':
            bcode = input("Book code: ")
            title = input("Title: ")
            sub = input("Subject: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            pickle.dump([bcode, title, sub, qty, price], f)

def SEARCH(bcode):
    with open('books.dat', 'rb') as f:
        while True:
            try:
                rec = pickle.load(f)
                if rec[0] == bcode:
                    print('Book found: ', rec)
                    break
            except:
                print("Book not found")
                break

APPEND()
bcode = input('Enter book code to search: ')
SEARCH(bcode)