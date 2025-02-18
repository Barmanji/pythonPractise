# Problem: Compute the factorial of a number using a while loop.
fact = 1
num = 0
while num > 0:
    fact *= num
    num -= 1
print(fact)


if num == 0 or 1:
    print("factorial of 0's and 1's are:", 1)
