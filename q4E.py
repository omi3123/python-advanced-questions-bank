"""
You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace these consecutive occurrences of the character 'c' with (4, c) in the string.
Input:
1222311
Output:
(1, 1) (3, 2) (1, 3) (2, 1)
"""
str1 = ("1222311")
dict1 = {}
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for k,v in dict1.items():
    print(k, v, end=" ", sep=",")
       