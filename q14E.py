"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
"""
def uniqInOrder(sequence):
    listR = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            listR.append(sequence[i])
    return listR
print(uniqInOrder("ABBCDAB"))        