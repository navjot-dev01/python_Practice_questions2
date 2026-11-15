                        # general method not consider good , time consuming

class Employee:
    company="ITC"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f'The name of the employee is {self.name} and salary is {self.salary}')

class Programmer:
    company="Microsoft"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f'The name of emplyee is {self.name} and salary is {self.salary}')

    def language(self,language):
        self.language=language
        print(f'The language of employee is {self.language}')

a=Employee()
a.show("rahul",120000)
b=Programmer()
b.show("rahul",5000000)
b.language("JS")

print(a.company,b.company)

# less time consuming method in intro2.py 

        