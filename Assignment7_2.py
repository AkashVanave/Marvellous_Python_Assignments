class Circle():

    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.area=0.0
        self.circumference=0.0

    def Accept(self,Radius):
        self.radius=Radius

    def CalculateArea(self):
        self.area=Circle.PI*self.radius**2

    
    def CalculateCircumference(self):
        self.circumference=2*Circle.PI*self.radius


    def display(self):
        print("Area of circle",self.area)
        print("Area of circumference",self.circumference)



def main():
    print("Enter the value of radius")
    no=int(input())

    obj1=Circle()
    obj1.Accept(no)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.display()


    obj2=Circle()
    obj2.Accept(no)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.display()




if __name__=="__main__":
    main()