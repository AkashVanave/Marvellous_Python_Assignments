def DisplayEven():
    cnt=0
    i=1
    while(cnt<10):
        if(i%2==0):
            print(i,end=" ")
            cnt=cnt+1
        i=i+1       
    

def main():
    DisplayEven()

if(__name__=="__main__"):
    main()
