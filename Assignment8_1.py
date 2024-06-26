class BookStore():

    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks+=1

    def Display(self):
        print("Name",self.Name)
        print("Author",self.Author)
        print("No of Books",BookStore.NoOfBooks)



obj1=BookStore("Linux System Programming","Robert Love")
obj1.Display()

obj2=BookStore("C programming","Denis Ritchie")
obj2.Display()


