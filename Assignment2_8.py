def displayPattern(freq):
    
    for i in range(freq):
        for j in range(i+1):
                print(j+1,end=" ")
               
        print()




def main():
    print("Enter the  number")
    A=int(input())

    Result1=displayPattern(A)
    
if __name__=="__main__":
    main()