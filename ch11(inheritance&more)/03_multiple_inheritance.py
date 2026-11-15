class Employee:
    company="ITC"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f'The name of the employee is {self.name} and salary is {self.salary}')

class Position:
    company="ITC"
    def printposition(self,position):
        self.position =position
        print(f"Position of the Employee is {self.position}")       

class Programmer(Employee,Position):
    company="Microsoft"
    
    def language(self,language):
        self.language=language
        print(f'The language of employee is {self.language}')

a=Employee()
b=Position()
c=Programmer()

c.show("harry",1200000)
c.language("Python")
c.printposition("Manager")

print(a.company,b.company,c.company)

# next file 01_multiple_inheritance.py