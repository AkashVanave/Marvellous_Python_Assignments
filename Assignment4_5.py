from functools import reduce

def Prime(Num):
    arr=list()

    if(Num<=1):
        return False
    else:
        for i in range (2, Num):
            if(Num%i==0):
                return False

            
    return True
    arr.append(i)



#Multiply=lambda No:No*2

#Max=lambda x,y: x if x > y else y

# def Max(data):
#     maxnum=data[0]
#     for i in data:
#         if(i>maxnum):
#             maxnum=i
#     return maxnum


def main():
    print("enter the total number")
    size=int(input())

    print("Enter the element in list")
    data=[]
    for i in range(size):
        no=int(input())
        data.append(no)

    print("List of Elements",data) 

    Fdata=list(filter(Prime,data))
    print("Data after filter",Fdata)

    Mdata=list(map(lambda No:No*2,Fdata))
    print("Data after map",Mdata)

    Rdata=reduce(lambda x,y: x if x > y else y,Mdata)
    print("Data after reduce",Rdata)
    



if __name__=="__main__":
    main()