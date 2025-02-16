import datetime
todayIs = datetime.datetime.now().strftime("%A")
age = int(input("Enter your age: "))

if todayIs == 'Wednesday':
    print("Its discount day becuase its Wednesday, $2 discount enjoy"),
    if age >= 18:
        print(f"Movie tickets is $10 for {age}yrs old")
    elif age == 1 or 2:
        print(f"Movie tickets is $6 for {age}yr old")
    else:
        print(f"Movie tickets is $6 for {age}yrs old")
else:
    print(f"Its not your lucky day becuase its {
          todayIs}, come Wednesday for discount"),
    if age >= 18:
        print(f"Movie tickets is $12 for {age}yrs old")
    elif age == 1 or 2:
        print(f"Movie tickets is $8 for {age}yr old")
    else:
        print(f"Movie tickets is $8 for {age}yrs old")


# could be done as - price = 12 if age >= 18 else 8
# price -= 2 if day/todayIs = Wednesday
