import os
import multiprocessing
import threading

def EvenFactor(No):
    x=0
    arr1=list()
    for i in range(1,No+1):
        if(No%i==0):
            arr1.append(i)
            x=x+i

    print("List of total Factors",arr1)

    y=0
    arr2=list()
    for j in arr1:
        if(j%2==0):
            arr2.append(j)
            y=y+j
        
    print("List of Even Factors",arr2)
    print("Addition of Even factor is",y)

def OddFactor(No):
    x=0
    arr1=list()
    for i in range(1,No+1):
        if(No%i==0):
            arr1.append(i)
            x=x+i

    print("List of total Factor",arr1)
    y=0
    arr2=list()
    for j in arr1:
        if(j%2!=0):
            arr2.append(j)
            y=y+j

    print("List of odd Factor",arr2)
    print("Addition of Odd factor is",y)


def main():
    print("Enter the frequency")
    Value=int(input())

    p1=threading.Thread(target=EvenFactor,args=(Value,))
    p2=threading.Thread(target=OddFactor,args=(Value,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()


    print("Exit from main")


if __name__=="__main__":
    main()