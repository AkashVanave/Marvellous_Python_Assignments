def chkPositive(No):
    if(No==0):
        print("Zero")
    elif(No>0):
        print("Postive Number")
    else:
        print("Negative Number")

def main():
    print("Enter a number: ")
    number=int(input())
    chkPositive(number)

if(__name__=="__main__"):
    main()
