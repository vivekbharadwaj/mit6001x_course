# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:55:52 2016

@author: Vivek
"""

# Some string gotchas

# define the strings
str1 = 'hello'
str2 = ','
str3 = 'world'
str4 = str1+str3

# do stuff with it

# 1) repeat something 3 times
str3 * 3 
# worldworldworld

# 2) substring only 'el' in 'hello'
str1[1:3]
# el

# 3) get everything in a string except the last character
#    i.e left(str,len(str)-1)
str3[:-1]
# worl

# 4) get only consecutive letters in a string
str4[1:9:2]
# elwr

# 5) reverse the string
str4[::-1]
# dlrowolleh

# 6) user input always returns string, even if the user inputs a number
result = int(input("enter a number here: "))

