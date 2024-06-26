import os


def main():
    print("Enter the file name")
    fname=input()

    if(os.path.exists(fname)):
        fobj=open(fname,"r")
        print("File is sucessfully opened")
        
        for i in fobj:
            print(i)    

        fobj.close()
        

    else:
        print("unable to open file as file is not present in current directory")

if __name__=="__main__":
    main()