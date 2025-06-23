"""
Write a function which will take an integer as input and print each digit in a separate line. You are not allowed to use str or any other method will convert the integer into string.
"""
def separateL(integer):
    while integer > 0:
        digit = integer % 10
        print(digit)
        integer = integer // 10
separateL(1011)
