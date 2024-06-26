def displayPattern(freq):
    
    for i in range(freq,0,-1):
        for j in range(0,i-1):
                print("*",end=" ")
               
        print()




def main():
    print("Enter the number")
    A=int(input())

    Result1=displayPattern(A)
    
if __name__=="__main__":
    main()