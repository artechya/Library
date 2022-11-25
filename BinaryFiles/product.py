import pickle

def CREATE():
    with open('product.dat', 'wb') as f:
        L = []
        while input('Add record? (y/n) ').lower() == 'y':
            pcode = input("Product Code: ")
            ptype = input("Product Type: ")
            pname = input("Product Name: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            L.append([pcode, ptype, pname, qty, price])
        pickle.dump(L, f)

def DISPLAY():
    print("PCode\tPType\tPName\tQty\tPrice")
    with open('product.dat', 'rb') as f:
        L = pickle.load(f)
        for rec in L:
            for element in rec:
                print(element, end='\t')
            print()

def DELETE(pcode):
    with open('product.dat', 'r+b') as f:
        L = pickle.load(f)
        for i in range(len(L)):
            if L[i][0] == pcode:
                print("Deleted record: ", L.pop(i))
                break
        else:
            print("Record not found")
            return
        f.seek(0)
        pickle.dump(L, f)
    print("Table after deletion: ")
    DISPLAY()


def SORT():
    with open('product.dat', 'r+b') as f:
        L = pickle.load(f)
        L.sort()
        f.seek(0)
        pickle.dump(L, f)
    print("Sorted records: ")
    DISPLAY()

def UPDATE(pcode, change):
    with open('product.dat', 'r+b') as f:
        L = pickle.load(f)
        for rec in L:
            if rec[0] == pcode:
                rec[3] += change
                break
        else:
            print("Record not found")
            return
        f.seek(0)
        pickle.dump(L, f)
    print("Updated records: ")
    DISPLAY()

CREATE()
DISPLAY()

pcode = input("Product code to delete: ")
DELETE(pcode)

SORT()

pcode = input("Product code to update: ")
change = int(input("Change in quantity: "))
UPDATE(pcode, change)
