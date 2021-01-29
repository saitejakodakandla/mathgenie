import os
mylist=[]
def add():
    '''
    this function adds item to the list
    '''
    item=input("Enter the item to add to the list")
    mylist.append(item)
    return main()

def display():
    for item in mylist:
        print(item)
    return main()

def itematindex():
    try:
        index=int(input("Enter the postion of the item"))
        print(mylist[index])
        return main()
    except IndexError:
        print("The position you are trying to access has no value,retry")
        return display()
    except ValueError:
        print("Incorrect Index , Index should be an Integer")

switcher={
    1:add,
    2:display,
    3:itematindex
}


def main():
    print("List Operations")
    print("1. Add item to the list")
    print("2. Display the list")
    print("3. Display item at a position")
    ch=int(input("Enter the operation number"))
    if ch>0 and ch<4:
        switcher.get(ch)()
    else:
        print("Invalid Operation Selected")
        return main()
    return 

if __name__=="__main__":
    main()
