def DisplayPattern2(freq):
    
    if(freq>0):   
        DisplayPattern2(freq-1)
        print(freq,end=" ")

def main():
    print("enter the freq")
    no=int(input())
    DisplayPattern2(no)


if __name__=="__main__":
    main()