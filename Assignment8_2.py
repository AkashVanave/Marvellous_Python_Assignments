class BankAccount():

    ROI=10.5
    Interest=0

    def __init__(self,name):
        self.Name=name
        self.Amount=0


    def Deposit(self,amt):
        self.Amount=amt
        print("Deposited amount",self.Amount)

    def Withdraw(self,amt):
        self.Amount=self.Amount-amt
        print("Amount after Withdraw",self.Amount)
    
    def CalculateInterest(self):
        BankAccount.Interest=self.Amount*BankAccount.ROI/100
        print("Interest",BankAccount.Interest)

    def Display(self):
        print("Name",self.Name)
        print("Amount",self.Amount)



obj1=BankAccount("Shubham")
obj1.Deposit(80000)
obj1.Withdraw(20000)
obj1.CalculateInterest()
obj1.Display()


obj2=BankAccount("Suraj")
obj2.Deposit(70000)
obj2.Withdraw(20000)
obj2.CalculateInterest()
obj2.Display()



    



        