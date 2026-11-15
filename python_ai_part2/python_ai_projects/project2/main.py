'''
We are going to write a program that generates a random number and asks the user to the guess it.
'''

import random
n=random.randint(1,100)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100. ")

guess=0
a=-1
while(a!=n):
    guess +=1


    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number please!")

    elif(a<n):
        print("Higher number please!")

print(f"You have guessed the number {n} correctly in {guess} attempts.")