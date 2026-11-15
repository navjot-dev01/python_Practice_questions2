class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f'The class number of a is {cls.a}')

    @property
    def name(self):
        return f'{self.fname} {self.lname}'
    
    @name.setter
    def name(self,value): 
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]      # DOUBT 

obj=Employee()
obj.a=45

obj.name="Harry Potter"
print(obj.name)

obj.show()