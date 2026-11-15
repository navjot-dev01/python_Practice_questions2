# Create  a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

p=Programmer("Harry",12000,1234) 
print(p.name,p.salary,p.id,p.company) 

r=Programmer("Rohan",13000,2345)
print(r.name,r.salary,r.id,r.company)
        