# this is not genuine method , very less readability


import random
'''
-1 for water
1 for snake
0 for gun
'''

print("w for Water , g for Gun and s for Snake")

computer=random.choice([1,-1,0])
choice=input("Enter your choice: ")
yourdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=yourdict[choice]

print(f'You chose { reversedict[you]} and computer chose {reversedict[computer]}')
if(you==computer):
    print("It's a draw")

# else:
#     if(computer==1 and you==-1):         1-(-1)=2
#         print("You lose!")

#     elif(computer==1 and you==0):       1-0=1
#         print("you  Win!")

#     elif(computer==-1 and you==1):      -1-1=-2
#         print("you Win!")  

#     elif(computer==-1 and you==0):     -1-0=-1
#         print("You Lose!")

#     elif(computer==0 and you==1):       0-1=-1
#         print("you Lose!")

#     elif(computer==0 and you==-1):     0-(-1)=1
#         print("you Win!")
                
#     else:
#         print("Something went wrong!")


elif((computer-you)==2 or (computer-you)==-1):
    print("You Lose !")

elif((computer- you)==2 or (computer-you)==1):
    print("You Win !")

else:  
    print("Something went wrong!")

