from MarvellousNum import ChkPrime

def ListPrime(Data):
    sum=0
    ret2=ChkPrime(Data)
    print("prime number list is",ret2)
    for i in ret2:
        sum=sum+i

    return sum


def main():
    print("Enter the numnber")
    size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("List of Elements user entered",data) 
    
    ret=ListPrime(data)
    print("sum of prime number", ret)


if __name__=="__main__":
    main()