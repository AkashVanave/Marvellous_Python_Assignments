import os

def main():
    print("Enter the file name from which u want to copy the data")
    fname1=input()

    print("Enter the file name to which u want to paste the data")
    fname2=input()

    if os.path.exists(fname1):
        fobj=open(fname1,"r")
        print("File is sucessfully opened")

        if os.path.exists(fname2):
            print("unable to create file already exists")
        else:
            fobj2=open(fname2,"a")
            print("File is sucessfully created")
            
        
        for i in fobj.readlines():
            fobj2.write(i)

        fobj.close()
        fobj2.close()
    
    else:
        print("unable to open file as file is not present in current directory")





if __name__=="__main__":
    main()