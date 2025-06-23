"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"This is an example!" ==> "sihT si na !elpmaxe"
"""
def rev_str(string):
    rev = ""
    access_words = string.split(' ')
    for word in access_words:
        slicing = word[-1::-1]
        rev += slicing
    return rev
print(rev_str("This is an example!"))