Multiply=lambda A,B:A*B

def main():
    print("Enter the first num")
    No1=int(input())

    print("Enter the second num")
    No2=int(input())

    ret=Multiply(No1,No2)
    print("Multiplication is ",ret)

if __name__=="__main__":
    main()