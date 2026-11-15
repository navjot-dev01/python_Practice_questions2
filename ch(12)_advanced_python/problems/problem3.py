#Write a list comprehension to print a list which contains the multiplication of 
# the user entered number.

n=int(input("Enter the number:"))

table=[n*i for i in range(1,11)]
print(table)