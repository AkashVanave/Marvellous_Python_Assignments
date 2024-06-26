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



def Findduplicate(path):

    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exist=os.path.isdir(path)

    dups={}
    if(exist):
        for folder,subfolder, files in os.walk(path):
            for file in files:
                path=os.path.join(folder,file)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

            return dups
    else:
        print("Invalid path")



def printduplicate(Dict1):
    results=list(filter(lambda x:len(x)>1, Dict1.values()))


    if len(results)>0:
        print("Duplicates found")

        print("Following files are Identical")

    iCnt=0
    for result in results:
        for subresult in result:
            iCnt+=1
            if(iCnt>=2):
                print('\t\t%s'%subresult)

        return subresult
    else:
        print("Duplicate not found")


def CreateLog(FileName,data):
    fd=open(FileName,'w')
    separator="-"*70

    fd.write(separator+"\n")
    fd.write("Log file created at"+time.ctime()+"\n")
    fd.write(separator+"\n")


    fd.write("Duplicate file name"+"\n")
    fd.write("%s\n"%data)
    fd.write(separator+"\n")

    fd.close()



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
        arr=Findduplicate(argv[1])
        arr2=printduplicate(arr)
        CreateLog("duplicates.log",arr2)
        endtime=time.time


    except ValueError:
        print("Invalid data type of input")

    except ValueError as E:
        print("Invalid Input",E)
    


if __name__=="__main__":
    main()