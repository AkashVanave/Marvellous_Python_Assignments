def Min(Data):
    min=Data[0]

    for i in Data:
        if(min>i):
            min=i

    return min

def main():
    print("Enter the number")
    Size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(Size):
        no=int(input())
        data.append(no)

    print("data in list",data)

    ret=Min(data)

    print("Minimum number from list is",ret)

if __name__=="__main__":
    main()