try:
    num=int(input("Enter the number:"))
    print(num) 

except Exception as e:
    print(e)

else:
    print("I am inside .")              # if there is no error then print else part too with try part