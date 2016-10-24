# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:51:19 2016

DESIGN YOUR OWN BISECTION SEARCH 
to find out secret number. This problem is an exercise

@author: Vivek
"""

# intro
print ("Please think of a number between 0 and 100!")

# define the variables
epsilon = 0.1
low = 0; high = 100
guess = int((low + high)/2)
userInput = 'x'

while userInput != 'c':
    print ("Is your secret number",str(guess)+"?")
    userInput = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    
    if userInput == 'h':
        high = guess
    elif userInput == 'l':
        low = guess
    elif userInput == 'c':
        break
    else:
        print ("Sorry, I did not understand your input.")
    
    guess = int((low + high)/2)

print ("Game over. Your secret number was:", guess)