import psutil
import time
import datetime
import schedule
import os
from sys import * 

def CreateLog(foldername):
    
    if not os.path.exists(foldername):
        os.mkdir(foldername)


    Filename=os.path.join(foldername,"Marvellous.log")

    fd=open(Filename,'w')

    arr=DisplayProcess()

    for i in arr:
        fd.write("%s\n"%i)


def DisplayProcess():
    listprocess=[]
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)
    
    return listprocess

    

    

    
def main():
    CreateLog(argv[1])


if __name__=="__main__":
    main()