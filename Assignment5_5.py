
Fact=1
def Factorial(No):
    global Fact
    
    if(No>=1):
        Fact = Fact * No
        No = No-1
        Factorial(No)
        
    return Fact
        



def main():
    print("Enter the freq")
    Value=int(input())
    Ret=Factorial(Value)

    print("Factorial of no is",Ret)
   

if __name__=="__main__":
    main()