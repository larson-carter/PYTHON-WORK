import datetime
now = datetime.datetime.now()
print("It is:")
print(now.year)

if (now.month) == 1:
    print("January")
elif (now.month) == 2:
    print("Feburary")
elif (now.month) == 3:
    print("March")
elif (now.month) == 4:
    print("April")
elif (now.month) == 5:
    print("May")
elif (now.month) == 6:
    print("June")
elif (now.month) == 7:
    print("July")
elif (now.month) == 8:
    print("August")
elif (now.month) == 9:
    print("September")
elif (now.month) == 10:
    print("October")
elif (now.month) == 11:
    print("November")
elif (now.month) == 12:
    print("December")
else:
    print("Error!")
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print("END OF PROGRAM")
