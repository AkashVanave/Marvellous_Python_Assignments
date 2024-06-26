def noofDigit(num):
    rem=0
    while(num!=0):
        rem=rem+num%10 
        num=int(num/10) 
        
    
    return rem

def main():
    print("Enter the number")
    A=int(input())
    Result=noofDigit(A)
    print("Sum of digit is",Result)

if __name__=="__main__":
    main()