class Employee:
    language="python"            # this is class attribute
    salary=1200000

    def getInfo(self):# what if i not write self check it which error occur
        print(f'The language is {self.language} and salary id {self.salary}')

    @staticmethod                  # decorator
    def greet():
        print("good morning")   # i am not able to use self.name and only name why?  

nav=Employee()
nav.name="Nav"
nav.greet()
nav.getInfo()

harry=Employee()
harry.name="Harry"
harry.greet()
'''
self refers to the instance of the class , it is automatically passed with function call from an object.
static method:
sometimes we need a function that does not use the self-parameter. 
'''