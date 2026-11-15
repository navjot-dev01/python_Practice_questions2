class Employee:
    language="Python"              # it work as default parameter as i pass actual argument
    salary=120000

    def __init__(self,name,salary,language):  # dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object.")

    def getInfo(self):
        print(f'The language is {self.language}. The salary is {self.salary}')

    @staticmethod
    def greet():
        print("good Morning")

harry =Employee("Harry",130000,"JS")
# harry.name="Harry"
harry.greet()
harry.getInfo()

# print(harry.name,harry.salary,harry.language)

# rohan=Employee()             it only doesn't work, all argument pass through it should get pass
