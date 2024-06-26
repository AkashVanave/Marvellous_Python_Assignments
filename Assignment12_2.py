import psutil
from sys import * 
import os
import time


def DisplayProcess(nameofprocess):

    print("")


    for proc in psutil.process_iter(['pid','name','username']):

        if nameofprocess in (proc.info['name'].lower()):
           
            print(proc.info)

    

    
def main():
    DisplayProcess(argv[1])


if __name__=="__main__":
    main()