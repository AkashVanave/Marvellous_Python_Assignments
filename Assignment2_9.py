def noofDigit(num):
    count=0

    while(num!=0):
        num=int(num/10)
        count+=1
    
    return count

def main():
    print("Enter the number")
    A=int(input())
    Result=noofDigit(A)
    print("Number of digit is",Result)

if __name__=="__main__":
    main()