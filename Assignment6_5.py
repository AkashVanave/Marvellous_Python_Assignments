import os
import multiprocessing
import threading

def thread1(num):
    for i in range(1,num+1):
        print(i)
  
    print("---------------")


def thread2(num):
    for i in range(num,0,-1):
        print(i)






def main():
    print("Enter the freq")
    no=int(input())
    
    p1=threading.Thread(target=thread1,args=(no,))
    p2=threading.Thread(target=thread2,args=(no,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

    print("End")


if __name__=="__main__":
    main()