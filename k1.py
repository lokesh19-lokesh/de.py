class Area:
    l=0
    b=0
    h=0
    def __init__(self,l1,b1,h1):
        self.l=l1
        self.b=b1
        self.h=h1
    def triangle(self):
        var1 = l * b * h
        print("triangle=",var1)
    def rectangle(self):
        var2=1/2*l*b*h
        print("rectangle=",var2)
obj = Area(77,99,77)