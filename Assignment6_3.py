import os
import multiprocessing
import threading

def EvenList(No):
    data1=list()
    x=0
    for i in (No):
        if(i%2==0):
            data1.append(i)
            x=x+i 
    print("Even number list",data1)
    print("Addition of even numbers",x)

def OddList(No):
    data2=list()
    x=0
    for i in No:
        if (i%2!=0):
            data2.append(i)
            x=x+i
    print("Odd number list",data2)
    print("Addition of Odd numbers",x)


def main():
    print("Enter the frequency")
    size=int(input())

    arr=list()
    print("Enter the list of number")
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)

    p1=threading.Thread(target=EvenList,args=(arr,))
    p2=threading.Thread(target=OddList,args=(arr,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
    print("End")


if __name__=="__main__":
    main()