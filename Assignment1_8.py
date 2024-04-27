def Display(No):
    for i in range(No):
        print("* ",end=" ")

def main():
    print("Enetr a number:")
    number=int(input())
    Display(number)

if(__name__=="__main__"):
    main()
