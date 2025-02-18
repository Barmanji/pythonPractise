givenStr = input("Give a string for reversal: ")
emptyStr = ""
for string in givenStr:
    emptyStr = string+emptyStr
print('Original String:', givenStr, '\nReversed String:', emptyStr)
if (givenStr == emptyStr):
    print("Given string was also a palindrome")
