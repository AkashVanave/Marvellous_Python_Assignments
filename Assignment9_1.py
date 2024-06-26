import os

def main():
    print("enter the file name that you want to check")
    fname=input()

    if os.path.exists(fname):
        print("File exists")
    else:
        print("file not exists")




if __name__=="__main__":
    main()