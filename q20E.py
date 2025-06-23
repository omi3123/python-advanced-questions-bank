"""
Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in the following way:
All the elements in the first and last row and column are 1.
All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
And so on …
Example: 
Given m = 10, n = 9, your function should return
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
 [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
 [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
 [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
 [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
 [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
"""
def create_pattern(m, n): 
    pattern = []
    for i in range(m):
        row = []
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                row.append(1)
            else:
                row.append(2)
        pattern.append(row)
    return pattern
print(create_pattern(10, 9))