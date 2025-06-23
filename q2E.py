"""
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
"""
words1 = ["1999","2000","1999","2100","H11"]
occur = {}
for i in words1:
    if i in occur:
        occur[i]+= 1
    else:
        occur[i] = 1
print(len(occur))
for i in occur.values():
    print(i, end=" ")