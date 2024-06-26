import os
import multiprocessing
import threading

def Small(str):
    smallchar=[]
    for char in (str):
        if char.islower():
            smallchar.append(char)

    print("Total small character in string",len(smallchar))
    print("Small character in string",smallchar)
   


def Capital(str):
    capitalchar=[]
    for char in (str):
        if char.isupper():
            capitalchar.append(char)

    print("Total Capital character in string",len(capitalchar))
    print("Capital character in string",capitalchar)



def Digits(str):
    digits=[]
    for char in (str):
        if char.isdigit():
            digits.append(char)

    print("Total Digit in string",len(digits))
    print("Digit character in string",digits)





def main():
    print("Enter the String")
    str=input()
    
    p1=threading.Thread(target=Small,args=(str,))
    p2=threading.Thread(target=Capital,args=(str,))
    p3=threading.Thread(target=Digits,args=(str,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

    p3.start()
    p3.join()


    print("End")


if __name__=="__main__":
    main()