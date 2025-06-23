"""
Split camel case
Complete the solution so that the function will break up camel casing, using a space between words.
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""   =>  ""
"""
def camelCaseSplit(string):
    sString = []
    for char in string:
        if char.isupper():
            sString.append(' ')
        sString.append(char)
    return ''.join(sString)
print(camelCaseSplit("camelCasing"))