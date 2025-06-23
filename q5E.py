"""
Remove symbols from the string
You are given a N x M grid of strings. It consists of alphanumeric spaces and characters, spaces, and symbols (!,@,#,$,%,&). To decode a string, you need to read each column and select only alphanumeric characters and concatenate them. If there are symbols between two alphanumeric characters of the decoded script, then replace them with empty string ‘’. You need to do this without using the if condition.
Input:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Output
This is Matrix#  %!
"""
N, M = 7, 3
grid = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]
decTerm = ""
for j in range(M):
    for i in range(N):
        characters = grid[i][j]
        decTerm += (characters.isalnum() * characters)
print(decTerm)