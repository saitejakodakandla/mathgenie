class Triangle:
    side1=0
    side2=0
    side3=0
    area=0
    name=""
    angleA=0.0
    angleB=0.0
    angleC=0.0

    # def __init__(self,name):
    #     self.name=name

    def __init__(self,s1,s2,s3)
        self.side1=s1
        self.side2=s2
        self.side3=s3
        print("Sides Set")
        return
    
    def getSides(self):
        print("Side 1:",self.side1)
        print("Side 2:",self.side2)
        print("Side 3:",self.side3)

    def area(self):
        a,b,c=self.side1,self.side2,self.side3
        s=(a+b+c)/2
        a=(s*(s-c)*(s-b)*(s-c))**0.5
        return a

    def write(self):
        filename=self.name+".csv"
        f=open(filename,"w+")
        print(self.side1,self.side2,self.side3,self.area(),sep=",",end="\n",file=f)
        f.close()
        


triangles=[]
t2=Triangle(3,5,12)
t2.write()

