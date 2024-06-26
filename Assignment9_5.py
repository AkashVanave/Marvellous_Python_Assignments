import os
import filecmp

def main():
    print("Enter the file name where u want to search the text")
    fname1=input()

    print("Enter the text")
    str1=input()
    

    if os.path.exists(fname1):
        fobj=open(fname1,"r")
        print("File is sucessfully opened")

        count=0
        file1=fobj.readlines()
  
        for i in file1:
            for j in i.split(" "): 
                print(j)
                if j==str1:
                    count=count+1
    
        print(count)




if __name__=="__main__":
    main()