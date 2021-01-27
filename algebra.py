import os
def add():
    total=0
    count=int(input("How many numbers do you want to add"))
    for i in range(count):
        v=int(input("Enter the Number"))
        total=total+v
    print("Total",total)
    return

def sub():
    return   

def multiply():
    return

switcher={
    1:add,
    2:sub,
    3:multiply
}

def main():
    print("Hi, I am in Algebra Mode now ")
    print("You can ask me to do the Following things")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Multiply Numbers")
    print("4. Divide Numbers")
    print("5. Divide to find the Remainder")
    print("6. Complex Numbers")
    print("0. Exit")
    ch=int(input("Enter the Number of the Operation"))
    if ch==0:
        return
    elif(ch<6 and ch>=0):
        func=switcher.get(ch)
        func()
    else:
        print("Invalid Operation, Please retry")
        return main()
    return main()
    
