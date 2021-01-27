import os
def circle():
    r=float(input("enter radius of a circle"))
    pi=22/7

    A=pi*(r**2)

    C=2*pi*r
    d=2*r

    print("area of a circle",A)
    print("Circumference of a circle",C)
    print("Diameter of a circle",d)
    return
def triangle():
    import math

   
   
    side1=float(input("enter the side1 of a triangle"))
    side2=float(input("enter the side2 of a triangle"))
    side3=float(input("enter the side3 of a triangle"))               
    if side1 <0 or side2 < 0 or side3<0:
         print("Invalid Values are Passed")
    else:
    
        s=(side1+side2+side3)/2
        uroot=s*(s-side1)*(s-side2)*(s-side3)
        area=math.sqrt(uroot)
    print(area)
    return
def rectangle():

    a=float(input("input of a"))
    b=float(input("input of b"))
    c=float(input("input of c"))

    A=a*b

    P=2*a+2*b

    q=((a**2)+(b**2))**(1/2)
    print("area of a rectangle",A)
    print("perimeter of a rectangle",P)
    print("polygon diagonals of a rectangle",q)
    return
def square():
    a=float(input("enter the value of a "))

    A = a**2


    P = 4*a
 

    q = a*(2**(1/2))


    s = q / (2**(1/2))
    print("side of a square is represented by s")
    print("Area of a square",A)
    print("perimeter of a square",P)
    print("polygon diagonals of a square",q)
    return
def equitorial_triangle():
    a=float(input("enter a side"))
    if a<0:
        print("Invalid values are passed")
    else:
        s = (3*a )/ 2
        K = ((3**(1/2))/4)  * (a**2)
        h = ((3**(1/2))/2) * a
        P = 3*a
        print("Semiperimeter of Equilateral Triangle",s)
        print("Area of Equilateral Triangle",K)
        print("Altitude of Equilateral Triangle",h)
        print("Perimeter of Equilateral Triangle",P)
        return
switcher={
    1:circle,
    2:triangle,
    3:rectangle,
    4:square,
    5:equitorial_triangle
}

def main():
    print("Hii,Iam in geometry mode now")
    print("You can ask me the following things")
    print("1.circle")
    print("2.triangle")
    print("3.rectangle")
    print("4.square")
    print("5.equitorial_triangle")
    print("0.exit")
    q=int(input("Enter the number of the operation"))
    if q==0:
        return
    elif(q<6 and q>=0):
        w=switcher.get(q)
        w()
    else:
        print("Invalid operation,please retry")
        return main()
    return main()


    
