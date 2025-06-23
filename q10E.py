"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
test => es
testing => t
A => A
"""
str1 = input("Enter a word: ")
len1 = len(str1)
midChar = len1 // 2
if len1 %2 == 0:
    print(str1[midChar-1:midChar+1])
else:
    print(str1[midChar])