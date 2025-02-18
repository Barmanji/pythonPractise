year = int(input("Check year is leap year or not\nPut year: "))
if year <= 0:
    print("Please provide a valid number")
    exit()

if ((year == int(year/4)*4) and year % 100 != 0) or int(year % 400 == 0):
    print("Leap")
else:
    print("NOt")

