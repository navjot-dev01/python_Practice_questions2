# simple example:

day=int(input("Enter the day in number from 1 to 7 :"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

                # and

# Matching multiple values 

num=int(input("Enter the number:"))
match num:
    case 1|2|3:
        print("Small number")
    case 4|5:
        print("Medium number")
    case _:
        print("Large number")  

     # and
# Match case with strings :

command=input(" choose command :")
match command:
    
    case "start":
        print("System started....")
    case "stop":
        print("System stopped....")
    case _:
        print("Unknown command....") 

# And
#  match case with list and tuple(powerful part) 

x= int (input("enter the value of x axis "))
y=int(input("Enter the value of y axis"))
point=(x,y)
match point:
    case (0,0):
        print("origin.") 
    case (0,y):
        print(" On y-axis.") 
    case (x,0):
        print("On x-axis.")
    case (x,y):
        print("Somewhere else.")            


        