def ChkDivision(No):
    if(No%5==0):
        return True
    else:
        return False

def main():
    print("Enter a number:")
    Number=int(input())

    result=ChkDivision(Number)

    print(result)

if(__name__=="__main__"):
    main()
