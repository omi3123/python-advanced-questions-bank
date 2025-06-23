"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ). You can not use the if statement.
"""
arr1 = { 6, 2, 1, 8, 10 }
result = sum(arr1)
total = result - min(arr1) - max(arr1)
print(total)