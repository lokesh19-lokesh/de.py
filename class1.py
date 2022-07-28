class Addition:
    first=0
    second=0
    answer=0

    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):#self because class funtion
        print("First number=",(self.first))
        print("second number=",(self.second))
        print("Addition of two number=", (self.answer))
    def calculate(self):
        self.answer=self.first+self.second

obj = Addition(1000,5000)#parameterized constructor
obj.calculate()
obj.display()
