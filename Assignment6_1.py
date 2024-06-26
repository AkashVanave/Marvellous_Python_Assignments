import os
import multiprocessing
import threading

def Even(No):
    print("List of Even numbers")
    a=2
    for i in range(No):
        print(a)
        a=a+2


def Odd(No):
    print("List of odd numbers")
    b=1
    for i in range(1,No):
        print(b)
        b=b+2


def main():
    print("Enter the frequency")
    Value=int(input())

    p1=threading.Thread(target=Even,args=(Value,))
    p2=threading.Thread(target=Odd,args=(Value,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()


    print("End")


if __name__=="__main__":
    main()