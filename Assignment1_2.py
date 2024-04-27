def ChkNum(Number):
    if(Number%2==0):
        return True
    else:
        return False
    
def main():
    print("Please enter the number:")
    num=int(input())
    result=ChkNum(num)
    if(result==True):
        print("Number is even.")

    else:
        print("Number is odd.")

if(__name__ =="__main__"):
    main()
