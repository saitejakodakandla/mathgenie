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
    k=int(input("Enter the greatest number"))
    s=int(input("Enter another number"))
    total=k-s
    print("Total",total)
    return   

def multiply():
    total=0
    count=int(input("How many numbers do You want to multiply"))
    for i in range(count):
        v=int(input("enter the number"))
        total=total*v
    print("Total",total)
    return
def divide():
    k=int(input("Enter the dividend"))
    a=int(input("Enter divisor"))
    quotient=k/a
    print("Quotient",quotient)
    return
def remainder():
    k=int(input("Enter the dividend"))
    a=int(input("Enter divisor"))
    remainder=k%a
    print("Remainder",remainder)
    return
def complexnumbers():
    print("Complex Number Arithmetic Enter Numbers in a+ij format")
    a=complex(input("Enter the first complex number"))
    b=complex(input("Enter the second complex number"))
    print(a+b,"is the Sum")
    print(a-b,"is the Difference")
    print(a*b,"is the product")
    return



switcher={
    1:add,
    2:sub,
    3:multiply,
    4:divide,
    5:remainder,
    6:complexnumbers,

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
    elif(ch<7 and ch>=0):
        func=switcher.get(ch)
        func()
    else:
        print("Invalid Operation, Please retry")
        return main()
    return main()
    
