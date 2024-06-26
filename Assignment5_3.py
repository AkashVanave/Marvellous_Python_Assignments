def DisplayPattern3(freq):

    if(freq>0):
        print(freq,end=" ")
        DisplayPattern3(freq-1)




def main():
    print("Enter the freq")
    no=int(input())
    DisplayPattern3(no)



if __name__=="__main__":
    main()