import math

def distance(x,y):
    dis=math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    return dis
class Shape():
    def __init__(self, name):
        self.name = name
class triangle(Shape):
    def __init__(self,coo,name):
        super().__init__(name)
        self.coo=coo
        self.p1=coo[0]
        self.p2=coo[1]
        self.p3=coo[2]
    def isValid(self):
        if(self.p1==self.p2 or self.p1==self.p3 or self.p2==self.p3):
            return False
        else:
            return True
    def area(self):
        a=distance(self.p1,self.p2)
        b=distance(self.p2,self.p3)
        c=distance(self.p1,self.p3)
        s=0.5*(a+b+c)
        area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area1
    def perimeter(self):
        side_a=distance(self.p1,self.p2)
        side_b=distance(self.p2,self.p3)
        side_c=distance(self.p1,self.p3)
        return side_a+side_b+side_c
class Circle(Shape):
    def __init__(self,center,radius,name):
        super().__init__(name)
        self.center=center
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return math.pi*2*self.radius
    def isValid(self):
        if self.radius>0:
            return True
        else:
            return False
class Rectangle(Shape):
    def __init__(self,coo,name):
        super().__init__(name)
        self.coo=coo
        self.p1=coo[0]
        self.p2=coo[1]
        self.p3=coo[2]
        self.p4=coo[3]
    def area(self):
        l=distance(self.p1,self.p2)
        w=distance(self.p2,self.p3)
        return l*w
    def perimeter(self):
        l=distance(self.p1,self.p2)
        w=distance(self.p2,self.p3)
        return 2*(l+w)
    def isValid(self,coo):
        for i in range(0,3):
            for j in range(i+1,4):
                if coo[i]==coo[j]:
                    return False
                    
        return True    
    
R=Rectangle(coo=[[-4,-3],[-4,-3],[3,1],[3,-3]],name="Rectangle")
print(R.area(),"  ",R.perimeter()," ",R.isValid(coo=[[-4,-3],[-4,-3],[3,1],[3,-3]]))
T=triangle(coo=[[-4,-3],[3,1],[3,1]],name="Triangle")
print(T.area(),"  ",T.perimeter()," ",T.isValid())
C=Circle(center=[1,1],radius=-4,name="Circle")
print(C.area(),"  ",C.perimeter()," ",C.isValid( ))

