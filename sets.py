def union():
    
    l1 = []
    num1 = int(input('Enter size of set 1: '))
    for n in range(num1):
        numbers1 = int(input('Enter any number:'))
        l1.append(numbers1)
 
    l2 = []
    num2 = int(input('Enter size of set 2:'))
    for n in range(num2):
        numbers2 = int(input('Enter any number:'))
        l2.append(numbers2)
 
    union = list(set().union(l1,l2))
 
    print('The Union of two sets is:',union)
    return

def intersection():
    l1 = []
    num1 = int(input('Enter size of set 1: '))
    for n in range(num1):
        numbers1 = int(input('Enter any number:'))
        l1.append(numbers1)
 
    l2 = []
    num2 = int(input('Enter size of set 2:'))
    for n in range(num2):
        numbers2 = int(input('Enter any number:'))
        l2.append(numbers2)
 
    intersection = list(set().intersection(l1,l2))
 
    print('The Intersection of two sets is:',intersection)
    return
def subtraction():
    l1=[]

    A = int(input("enter size of set 1"))
    for n in range(A):
        number1=int(input("enter a number:"))
        l1.append(number1)
        l2 = []
    B=int(input("enter the size of set 2"))
    for n in range(B):
        number2= int(input("enter a number:"))
        l2.append(number2)
    l1set,l2set=set(l1),set(l2)
    print("Difference of Set1 to Set2")
    printuncommon(l1set,l2set)
    print("Difference of Set2 to Set1")
    printuncommon(l2set,l1set) 
    return
def complement():
    l1=[]
    A=int(input("enter size of set1 :"))
    for n in range(A):
        number1=int(input("Enter a number:"))
        l1.append(number1)
        l2=[]
    B=int(input("Enter the size of set2:"))
    for n in range(B):
        number2=int(input("enter a number"))
        l2.append(number2)
    union = list(set().union(l1,l2))
    
    complement =printuncommon(l1,l2)
    print("is the complement of A")

    

  
switcher={
    1:union,
    2:intersection,
    3:subtraction,
    4:complement

}

def printuncommon(set1,set2):
    for i in set1:
        if i in set2:
            continue
        else:
            print(i)

def main():
    print("Hi, I am in Sets Mode now ")
    print("You can ask me to do the Following things")
    print("1. Union")
    print("2. Intersection")
    print("3. subtraction")
    print("4. complement")
    
    print("0. Exit")
    ch=int(input("Enter the Number of the Operation"))
    if ch==0:
        return
    elif(ch<5 and ch>=0):
        func=switcher.get(ch)
        func()
    else:
        print("Invalid Operation, Please retry")
        return main()
    return main()