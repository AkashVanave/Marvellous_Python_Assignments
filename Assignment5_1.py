i=1

def DisplayPattern(freq):
    global i
  
    if(freq>=i):
        print("*",end=" ")
        freq=freq-1
        DisplayPattern(freq)
        
        
def main():
    print("Enter the freq")
    freq=int(input())
    DisplayPattern(freq)
   

if __name__=="__main__":
    main()