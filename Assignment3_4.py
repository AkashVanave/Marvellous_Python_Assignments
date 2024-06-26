def frqofNumber(Data,n):
    Cnt=0
    for i in Data:
        if(i==n):
            Cnt=Cnt+1

    return Cnt





def main():
    print("Enter the numnber")
    size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("List of Elements",data)
    
    print("Enter the number for which u want the frequency")
    n=int(input())
    ret=frqofNumber(data,n)

    print("frequency of number in list", ret)


if __name__=="__main__":
    main()