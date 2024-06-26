import os
import filecmp

def main():
    print("Enter the first file name")
    fname1=input()

    print("Enter the Second file name")
    fname2=input()

    if os.path.exists(fname1):
        fobj=open(fname1,"r")
        print("File is sucessfully opened")

        if os.path.exists(fname2):
            fobj2=open(fname2,"r")
            print("File is sucessfully opened")
       
            
        file1=fobj.readlines()
        file2=fobj2.readlines()

        for i in range(len(file1)):
            if file1[i] !=file2[i]:
                print("Line "+str(i+1)+"  Does not match")
            else:
                print("Line "+str(i+1)+"  match")

            print("File 1",file1[i])
            print("File 2",file2[i])
       


        fobj.close()
        fobj2.close()
    
    else:
        print("unable to open file as file is not present in current directory")





if __name__=="__main__":
    main()