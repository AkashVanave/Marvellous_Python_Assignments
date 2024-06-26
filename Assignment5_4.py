def DisplayPattern3(freq):
    sum=0
    if(freq!=0):
        rem=freq%10   
        num=freq//10    
        sum=rem+DisplayPattern3(int(num))
    return sum


def main():
    print("Enter the freq")
    no=int(input())
    ret=DisplayPattern3(no)
    print("Sum is",ret)


if __name__=="__main__":
    main()