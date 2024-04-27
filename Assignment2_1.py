#Arithmetic Module
def Add(No1,No2):
    Ans=No1+No2
    return Ans

def Sub(No1,No2):
    Ans=No1-No2
    return Ans

def Div(No1,No2):
    Ans=No1/No2
    return Ans

def Mul(No1,No2):
    Ans=No1+No2
    return Ans


#Assignment code
import Arithmetic

def main():
    print("Enter first number: ")
    Number1=int(input())
    print("Enter Second number: ")
    Number2=int(input())

    Result=Arithmetic.Add(Number1,Number2)
    print("Addition is : ",Result)

    Result=Arithmetic.Sub(Number1,Number2)
    print("Subtraction is : ",Result)

    Result=Arithmetic.Div(Number1,Number2)
    print("Division is : ",Result)

    Result=Arithmetic.Mul(Number1,Number2)
    print("Multiplication is : ",Result)

if(__name__=="__main__"):
    main()
