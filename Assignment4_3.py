from functools import reduce


Compare=lambda No:((No>=70) & (No<=90))
Increase=lambda No:No+10
Mul=lambda No1,No2:No1*No2

def main():
    data=[]
    print("Enter the total list element")
    size=int(input())

    print("Enter the list element")

    for i in range(size):
        no=int(input())
        data.append(no)

    print("list of element",data)

    Fdata=list(filter(Compare,data))
    print("After filter data",Fdata)

    
    Mdata=list(map(Increase,Fdata))
    print("After Map data",Mdata)

    Rdata=reduce(Mul,Mdata)
    print("After Reduce data",Rdata)

if __name__=="__main__":
    main()