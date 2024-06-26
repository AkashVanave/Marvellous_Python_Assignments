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
        please find attched doc which contain log of running process.
        log file is created at : %s

        Thanks and Regards,
        Shubham
        """%(toaddr,time)

        Subject="""
        Marvellous Infosystem process log generated at : %s
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
        s.login(fromaddr," ")  #Add 16 char String code 
        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)
        s.quit()

    except Exception as E:
        print("unable to send mail ", E)


def ProcessLog(log_dir,rec_mailid):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(timestamp))

    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous infosystem process logger:"+timestamp+"\n")
    f.write(separator+"\n")
    f.write("\n")


    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    for element in listprocess:
        f.write("%s\n"%element)

    print("log file successfully generated at location %s",(log_path))


    connected=is_connected()

    if connected:
        starttime=time.time()
        Mailsender(log_path,time.time,rec_mailid)
        endtime=time.time()


        print("Took %s seconds to send mail"%(endtime-starttime))
    else:
        print("There is no internet connection")











def main():
    print("---------------- Marvellous Infosysytem -------------------")

    print("Application Name"+argv[0])

    if(len(argv) != 4):
        print("Error:Invalid number of argument")
        exit()


    if(argv[1] == "--h") or (argv[1] == "--H"):
        print("This script is used to perform Directory traversal and display checksum of files")
        exit()

    if(argv[1] == "--u") or (argv[1] == "--U"):
        print("Usage of the script : ")
        print("Applicationname  Absolute_of_directory_Extentipon ")
        exit()

   
    try:

        ProcessLog(sys.argv[2],sys.argv[3])


    except ValueError :

        print("Invalid data type of input")

    except Exception as E:
        print("Invalid input ", E)
            

    
    print("--------- Thank you for using our script -------------")
    print("------------- Marvellous Infosystems -----------------")

if __name__ == "__main__":
    main()

