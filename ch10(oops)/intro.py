# class Employee:
#     name="Nav"
#     language="python"
#     salary=1200000

# nav=Employee()
# print(nav.name,nav.language,nav.salary)

# harry=Employee()
# print(harry.salary,harry.language)    #  harry.name=nav

'''
objects of a give class can be involve the methods available to it without revealing the implementation 
details to the user- Abstraction and  Encapsulation

Noun = class = Employee
Adjective = atributes = name, language, salary
Verbs = Methods = getSalary(),increment()
'''

class Employee:
    language="python"            # this is class attribute
    salary=1200000

nav=Employee()
nav.name="Nav"    # this is instance attribute
print(nav.name,nav.language,nav.salary)

harry=Employee()
harry.name="Harry"
print(harry.name,harry.salary,harry.language)

#Here name is instance attribute and salary,language are class attribute as they directly belongs to the class