class Triangle:   # abstract class
    ab=0
    bc=0
    ac=0
    A=0
    B=0
    C=0
    def __init__():
        pass

    def showSides(self):
        print("Side 1: ab =>",self.ab)
        print("Side 2: bc =>",self.bc)
        print("Side 3: ac =>",self.ac)
        return

    def getArea():
        pass

    
class Scalane(Triangle):
    def __init__(self,ab,bc,ac):
        self.ab=ab
        self.bc=bc
        self.ac=ac
        return

    def __e__():
        return False

    def __add__(self,anotherTriangle):
        anotherTriangle.ab+=self.ab
        anotherTriangle.bc+=self.bc
        anotherTriangle.ac+=self.ac
        return anotherTriangle


    def getArea(self):
        if ab==bc==ac==0:
            print("Sides are not Set ")
            return -1
        else:
            area=98
            return area


class RightAngleTriangle(Triangle):
    base=0
    height=0

    def __init__(self,base,height):
        self.base=base
        self.height=height
        bc=base
        ab=height
        ac=((ab**2) + (bc**2) )**0.5
        return

    def getHypotenuse(self):
        return self.ac

    def getArea(self):
        return (0.5*self.base*self.height) 



myrt=RightAngleTriangle(3,5)
print(myrt.getHypotenuse())