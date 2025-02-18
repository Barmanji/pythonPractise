number = int(input("Give a number to multiply by: "))

for mutl_by in range(1, 10+1):
    if mutl_by == 5:
        continue
    print(f'{number} * {mutl_by}:', number * mutl_by)
