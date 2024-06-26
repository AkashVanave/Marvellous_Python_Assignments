def PrimeNumber(num):
    flag=False
    if(num==1):
        print("Number is not prime")
    elif(num>1):
        for i in range (2, num):
            if(num%i==0):
                flag=True

                break

        if(flag):
            print("Number is not prime")
        else:
            print("Number is prime")            

def main():
    print("Enter the number")
    A=int(input())
    Result1=PrimeNumber(A)

if __name__=="__main__":
    main()