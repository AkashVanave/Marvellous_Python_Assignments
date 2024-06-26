def MaxNum(Data):
    Maxnum=Data[0]

    for i in Data:
        if(Maxnum<i):
            Maxnum=i
    
    return Maxnum


def main():
    print("Enter the number")
    Size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(Size):
        no=int(input())
        data.append(no)

    print("Numbers are",data)

    ret=MaxNum(data)

    print("Max number from list is",ret)


if __name__=="__main__":
    main()