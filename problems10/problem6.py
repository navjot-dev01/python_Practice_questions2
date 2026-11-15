# Can you change the self-parameter inside a class to something else(say "harry"). Try changing self to 
# "slf" or "harry" and see others

from random import randint

class Train:
    def __init__(slf,trainNo):
         slf.trainNo=trainNo
        

    def book(sel,fro,to):      # from is user defined so i write it fro   
        print(f'Ticket is booked in train no. {sel.trainNo} from {fro} to {to}')

    def getStatus(harry):
        print(f'Train no. {harry.trainNo} is running on time') 

    def getFare(self,fro ,to):
        print(f'Ticket fare of train no.{self.trainNo} from {fro} to {to} is {randint(222,555)}')    

t=Train(12345)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")