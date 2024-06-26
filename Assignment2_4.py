def Addoffactors(num):
    fact=0
    for i in range(1,num):
        if(num%i==0):
           fact+=i 
    
    return fact

def main():
    print("Enter the first number")
    A=int(input())

    Result1=Addoffactors(A)
    print("Addition of factors",Result1)

if __name__=="__main__":
    main()