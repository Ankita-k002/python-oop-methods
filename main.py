"""there are 3 types of methods in class:
-> instance methods , uses instnaces of object, has access to objects parameters
-> class methods , bounded to the class itself, have access to class attributes/variable, they recieve the class itself (cls) as the first arguments
-> static methods, don't use /utilise/involve either instances (self) or the class attribute(cls)

"""

class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
 
    # Instance method(default)
    def get_info(self):
        return f"The name is {self.name} and the salary is {self.salary}."
    
    #static method
    @staticmethod #(we use decorator static method to not involve the self, value or attributes here but only the two values we typed)
    def sum(a,b):
        return a+b
    
    #Class methods
    @classmethod
    def get_company(cls):
        print(cls.company)  # function that takes class variable/attribute in a function form to easy acess

    @classmethod   #the first argument in class method is cls, second is what we will assign/give/want to change into
    def change_company(cls,new_company): #function for easily change/update the company(class attribute/state)
        cls.company=new_company
    
    


e1=Employee("Jack", 35000)
e2=Employee("Jill", 35000)
#print(e1.get_info())

e1.get_company()  # prints the original variable of the comapny 
e1.change_company("Acer")  # updates the company variable to the new variable that we gave
e1.get_company()   # prints the updated company variable
