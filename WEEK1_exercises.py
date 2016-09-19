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
import string
alpha_dict = dict(zip(string.ascii_lowercase,range(26)))

counter = 0
while counter < len(s):



list1 = ['bo','beggh','akl']
dict2 = dict(zip([len(x) for x in list1],list1))
sorted(dict2.items(), key=lambda x:x[0], reverse = True)[0][1]