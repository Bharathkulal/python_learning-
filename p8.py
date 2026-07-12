#decision making 


num = 10

if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


signal = input("enter the signal colure")

if signal == "red":
    print("stop")
elif signal== "yellow":
    print("get ready!!!!")
else:
    print("go")



gender = input("enter the gender  ")
age = int(input("enter the age  "))
is_student = False

if gender == "female":
    print("bus ticket is free")
else:
    if age <=12:
        print("child discount")
    elif age >=60:
        print("senior citizen discount")

        if is_student:
            print("student discount")
    else:
        print("full ticket price")

