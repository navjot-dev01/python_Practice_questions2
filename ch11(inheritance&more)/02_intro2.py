class Employee:
    company="ITC"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f'The name of the employee is {self.name} and salary is {self.salary}')

class Programmer(Employee):
    company="Microsoft"
    # def show(self,name,salary):                        [ NO NEED TO WRITE ]      
    #     self.name=name
    #     self.salary=salary
    #     print(f'The name of emplyee is {self.name} and salary is {self.salary}')

    def language(self,language):
        self.language=language
        print(f'The language of employee is {self.language}')

a=Employee()
b=Programmer()

b.show("harry",1200000)
b.language("Python")

print(a.company,b.company)