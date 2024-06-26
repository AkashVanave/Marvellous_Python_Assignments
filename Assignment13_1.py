from sys import * 
import hashlib
import os
import time
import psutil
import urllib
import sys
from urllib.request import urlopen
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def DeleteFiles(Dict1):
    results=list(filter(lambda x:len(x)>1,Dict1.values()))

    print(results)

    if len(results)>0:
        print("Duplicates found")

        iCnt=0
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    os.remove(subresult)
                    print(subresult+"File deleted at"+time.ctime())
            iCnt=0

    else:
        print("No duplicates found")

    
   



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

    flag = os.path.isabs(path)

    if (flag == False):
        path = os.path.abspath(path)
        
    exist = os.path.isdir(path)

    dups={}
    if(exist):
        for dirName, subdirs, fileList in os.walk(path):
            print("current folder name"+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
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
        duplicates=[]
        for result in results:
            for subresult in result:
                iCnt+=1
                if(iCnt>=2):      
                    print('\t\t%s'%subresult)   
                    #os.remove(subresult)
                    duplicates.append(subresult)
            iCnt=0  
        return duplicates
    else:
        print("Duplicate not found")




def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com/',timeout=1)
        return True

    except urllib.error as err:
        return False


def Mailsender(FileName,time,mailid):
    try:
        fromaddr=""
        toaddr=mailid

        msg=MIMEMultipart()

        msg['from']=fromaddr
        msg['To']=toaddr

        body="""
        Hello %s
        Welcome to marvellous Infosystem
        please find attched doc which contain Information of Duplicates files in Specified folder.
        Below are the Duplicate files.%s

         

    




        Thanks and Regards,
        Shubham
        """%(toaddr,time)

        Subject="""
        Marvellous Infosystem Duplicate files : %s
        """%(time)


        msg['Subject']=Subject
        msg.attach(MIMEText(body,'plain'))

        attachment=open(FileName,'rb')
        p=MIMEBase('application','octlet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachedment; filename= %s"%FileName)

        msg.attach(p)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr," ")  #Add 16 char string code 
        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)
        s.quit()

    except Exception as E:
        print("unable to send mail ", E)


def CreateLog(data,log_dir="Marvellous"):
    
    print(data)
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    CreateLog.log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(timestamp))

    f=open(CreateLog.log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous infosystem Duplicates files:"+timestamp+"\n")
    f.write(separator+"\n")
    f.write("\n")


    f.write("Duplicate file name"+"\n")

    for i in data:
        f.write("%s\n"%i)
        f.write(separator+"\n")

    f.close()



def ProcessLog(rec_mailid):
    
    connected=is_connected()

    
    log_path=CreateLog.log_path
    print(log_path)

    if connected:
        starttime=time.time()
        Mailsender(log_path,time.time,rec_mailid)
        endtime=time.time()


        print("Took %s seconds to send mail"%(endtime-starttime))
    else:
        print("There is no internet connection")




def main():

    print("Application Name is :"+argv[0])
    print(int(argv[2]))


    if(len(argv)!=4):
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
        arr={}
        arr=Findduplicate(argv[1])
        print(arr)
        print("------------------------------------------------------------------------------------------------------------")
        arr2=printduplicate(arr)
        print(arr2)
        print("------------------------------------------------------------------------------------------------------------")
        CreateLog(arr2)
        ProcessLog(argv[3])


        schedule.every(int(sys.argv[2])).minutes.do(DeleteFiles,arr)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
            
    except ValueError:
        print("Invalid data type of input")

    except ValueError as E:
        print("Invalid Input",E)
    


if __name__=="__main__":
    main()


#filename.py Demo 50   mailid
#     0       1   2       3    


#duplicate find-> crete log -> delete that files ->mail send

#python Assignment13_1.py Demo 1 aks@gmail.com