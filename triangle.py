
from input import Area

class triangle(Area):
    def __init__(self, l,b,h):
        super().__init__(l,b,h)
        var1 = l * b * h
        print("triangle=", var1)
obj.triangle()