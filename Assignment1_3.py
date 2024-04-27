def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    print("Enetr first number:")
    No1=int(input())
    No2=int(input())
    result=Add(No1,No2)
    print("Addition is : ",result)

if(__name__=="__main__"):
    main()
