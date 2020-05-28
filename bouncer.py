# ask age
# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry

age = input("What is your age: ")

if age != " ":
    age = int(age)

    if age >= 18 and age < 21:
        print("Your age is less then 21 you allowed in with wristband")

    elif age >= 21:
        print("You allow to enter and have drinks")

    else:
        print("Too young not allowed")


else:
    print("Enter your age please")
