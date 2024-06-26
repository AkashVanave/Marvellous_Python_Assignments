def ChkPrime(Data):
    arr=list()

    for i in Data:
        count=0
        if (i>1):
            for j in range (1, i):
                if(i%j==0):
                    count+=1

            if(count==1):
                arr.append(i)

    #print("prime list",arr)
    return arr

def main():
    print("Enter the numnber")
    size=int(input())

    data=list()
    print("Enter the list of number")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("List of Elements",data) 
    
    ret=ChkPrime(data)
    print("prime number list is", ret)


if __name__=="__main__":
    main()



