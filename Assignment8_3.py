class Number():
    
    def __init__(self,val):
        self.Value=val 


    def ChkPrime(self):
        flag=False
        if self.Value > 1:
            for i in range(2,self.Value):
                if(self.Value%i==0):
                    flag=True

                    break

            if flag:
                print(self.Value,"is not prime")
            else:
                print(self.Value,"is prime")


    def ChkPerfect(self):
        flag=False
        
        sum=0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                sum=sum+i

        if(sum==self.Value):
            flag=True
            print(self.Value, "is perfect number")
        else:
            flag=False
            print(self.Value, "is not perfect number")


    def Chkfactor(self):
        
        arr=list()
        for i in range (1,self.Value+1):
            if(self.Value%i==0):
                arr.append(i)

        return arr


    def SumOffactor(self):
        print("factors of number is",self.Chkfactor())
        ret=self.Chkfactor()
        sum=0
        for i in ret:
            sum=sum+i

        print("Sum of factors is",sum)


obj1=Number(6)
obj1.ChkPrime()
obj1.ChkPerfect()
obj1.Chkfactor()
obj1.SumOffactor()

obj2=Number(11)
obj2.ChkPrime()
obj2.ChkPerfect()
obj2.Chkfactor()
obj2.SumOffactor()



