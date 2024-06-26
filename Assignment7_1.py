class Demo():

    Value=0
    
    def __init__(self,num1,num2):
        print("Inside Constructor")
        self.no1=num1
        self.no2=num2

    def fun(self):
        print("inside fun")
        print("value of num1",self.no1)
        print("value of num2",self.no2)

    def gun(self):
        print("inside gun")
        print("value of num1",self.no1)
        print("value of num2",self.no2)

obj1=Demo(11,21)
obj2=Demo(51,101)



print("Value of num1 from obj1:",obj1.no1)
print("Value of num2 from obj1:",obj1.no2)

print("Value of num1 from obj2:",obj2.no1)
print("Value of num2 from obj2:",obj2.no2)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()

    
