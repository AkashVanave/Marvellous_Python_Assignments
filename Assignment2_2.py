def Display(No):
    for j in range(No):
        for i in range(No):
            print("*",end=" ")
        print()
        
def main():
    print("Enetr number:")
    number=int(input())

    Display(number)

if(__name__=="__main__"):
    main()
