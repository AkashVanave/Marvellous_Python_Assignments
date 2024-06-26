power=lambda No:No**2

def main():
    print("Enter the number")
    num=int(input())

    ret=power(num)
    print("power of 2 of num is", ret)



if __name__=="__main__":
    main()