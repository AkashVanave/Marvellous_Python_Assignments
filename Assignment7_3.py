class Arithmatic():

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self,Value1,Value2):
        self.no1=Value1
        self.no2=Value2

    def Addition(self):
        self.Add=self.no1+self.no2

    def Subtraction(self):
        self.Sub=self.no1-self.no2

    def Multiplication(self):
        self.Mul=self.no1*self.no2

    def Division(self):
        self.Div=self.no1/self.no2

    def Display(self):
        print("Addition is",self.Add)
        print("Subtraction is",self.Sub)
        print("Multiplication is",self.Mul)
        print("Division is",self.Div)

def main():
    print("Enter the first num")
    num1=int(input())
    print("Enter the 2nd number")
    num2=int(input())

    obj1=Arithmatic()
    obj1.Accept(num1,num2)

    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()
    obj1.Display()

if __name__=="__main__":
    main()