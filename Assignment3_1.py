def Addition(data):
    sum=0
    for i in data:
        sum=sum+i
    
    return sum


def main():
    print("Enter the number")
    Size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(Size):
        no=int(input())
        data.append(no)

    print("List is",data)

    ret=Addition(data)
    print("Addition is",ret)


if __name__=="__main__":
    main()