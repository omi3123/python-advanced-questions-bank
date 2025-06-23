"""
You are given a positive integer. You can only use one for loop and one print statement. Print a numerical triangle of height like the one below:
Input:
5
Output:
1
22
333
4444
"""
var_1 = 5
for i in range(1, var_1):
    print(str(i) * i)