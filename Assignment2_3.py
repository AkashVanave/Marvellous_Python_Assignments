def factorial(freq):
    fact=1
    for i in range(1,freq):
        fact+=fact*i
    
    return fact

def main():
    print("Enter the first number")
    A=int(input())

    Result1=factorial(A)
    print("factorial of number is",Result1)

if __name__=="__main__":
    main()