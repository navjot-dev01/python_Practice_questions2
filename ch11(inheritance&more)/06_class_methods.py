class Employee:
    a=1
    # def show(self):                                   It show INSTANCE value
    #     print(f'The class value a is {self.a}') 
     
    @classmethod 
    def show(cls):
        print(f'The class value a is {cls.a}')           

obj=Employee()
obj.a= 45             

obj.show()

