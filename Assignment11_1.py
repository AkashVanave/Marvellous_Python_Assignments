from sys import * 
import os
import time
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()



def DisplayChecksum(path):

    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exist=os.path.isdir(path)

    if(exist):
        for folder,subfolder, files in os.walk(path):
            for file in files:
                path=os.path.join(folder,file)
                file_hash=hashfile(path)

                print(path)
                
                print(file_hash)



def main():

    print("Application Name is :"+argv[0])


    if(len(argv)!=2):
        print("Invalid number of inputs")
        exit()


    if(argv[1] == "--h") or (argv[1] == "--H"):
        print("This script is used to perform Directory traversal and display checksum of files")
        exit()

    if(argv[1] == "--u") or (argv[1] == "--U"):
        print("Usage of the script : ")
        print("Applicationname  Absolute_of_directory_Extention")
        exit()

    
    try:
        starttime=time.time
        DisplayChecksum(argv[1])
        endtime=time.time


    except ValueError:
        print("Invalid data type of input")

    except ValueError as E:
        print("Invalid Input",E)
    


if __name__=="__main__":
    main()