"""
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p. we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""
int1 = 695
sum = 0
pow = 2
for i in str(int1):
    sum += int(i) ** pow
    pow += 1
if sum % pow == 0:
    k = sum/int1
    print(f"{sum} = {int1} * {int(k)}")