# -*- coding: utf-8 -*-
"""
Week 1 exercises for the MIT 6.00.1x course
"""

s = 'azcbobobegghakl'

# Q1
# Write a program that counts up the number of vowels contained in the string 
# s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
# s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

vow = 0
for letter in s:
    vow = vow + ('a' in letter)+('e' in letter)+('i' in letter)+('o' in letter)+('u' in letter)
print ("Number of vowels: ",vow)

# Q2
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2
bob = 0
for index in range(0,len(s)-2):
    if s[index]+s[index+1]+s[index+2] == 'bob':
        bob += 1
print ("Number of times bob occurs is: ",bob)

# Q3
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then 
# your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print
# Longest substring in alphabetical order is: abc


# define a dictionary of indices for each letter of the alphabet
import string
alpha_dict = dict(zip(string.ascii_lowercase,range(26)))

# define a function that returns the largest alphabetical substring from the 
# beginning of a string
def return_largest_alphabetical_part(substr):
    alphabet_value = 0
    alphabetical_substr_part = ''
    for letter in substr:
        if alpha_dict[letter] < alphabet_value:
            break
        alphabetical_substr_part += letter
        alphabet_value = alpha_dict[letter]
    return alphabetical_substr_part

# main function to progressively loop through different starting points of 
# the overall string and call the above function iteratively
longest_alphabetical_substring = ''
counter = 0
while counter <= len(s):
    if len(return_largest_alphabetical_part(s[counter:])) > len(longest_alphabetical_substring):
        longest_alphabetical_substring = return_largest_alphabetical_part(s[counter:])
    counter+= 1
print ("Longest substring in alphabetical order is: ",longest_alphabetical_substring)