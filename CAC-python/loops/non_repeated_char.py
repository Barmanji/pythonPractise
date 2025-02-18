# Problem: Given a string, find the first non-repeated character.

givenStr = "Nitin"
# count = 0
# lowerGivenStr = givenStr.lower()
#
# for char in lowerGivenStr:
#     for nestChar in lowerGivenStr:
#         if char == nestChar:
#             count += 1
#             if count == 0:
#                 break
#
for chat in givenStr.lower():
    if givenStr.lower().count(chat) == 1:
        print(chat)
        break
