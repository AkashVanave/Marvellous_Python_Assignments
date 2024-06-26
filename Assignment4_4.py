from functools import reduce


even=lambda No:(No%2==0)
square=lambda No:No**2
Add=lambda No1,No2:No1+No2


def main():
    print("enter the total number")
    size=int(input())

    print("Enter the element in list")
    data=[]
    for i in range(size):
        no=int(input())
        data.append(no)

    Fdata=list(filter(even,data))
    print("Data after filter",Fdata)

    Mdata=list(map(square,Fdata))
    print("Data after map",Mdata)

    Rdata=reduce(Add,Mdata)
    print("Data after reduce",Rdata)
    



if __name__=="__main__":
    main()