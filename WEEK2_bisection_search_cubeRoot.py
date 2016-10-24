# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 08:41:19 2016

DESIGN YOUR OWN BISECTION SEARCH 
to find out cube root for all real numbers

@author: Vivek
"""

# define the variables
user_input = float(input("Please enter a number:"))
epsilon = 0.01
numGuesses = 1
negative_number_multiplier = 1

# initialise highs and lows based on the input provided
x = abs(user_input)

if x == 1:
    low = 2; high = 0
elif x < 1:
    low = x; high = 1
else:
    low = 1; high = x
    
guess = (low + high)/2.0

while abs(guess**3 - x )>= epsilon:
    if guess**3 >= x:
        high = guess
    else:
        low = guess
    guess = (low + high)/2.0
    numGuesses += 1

if x != user_input:
    negative_number_multiplier = -1
    
print ("numGuesses is:",numGuesses)
print ("answer is:",negative_number_multiplier*guess)
print ("answer cubed is:", negative_number_multiplier*guess**3)