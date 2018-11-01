import datetime
currentDate = datetime.datetime.now()
year = currentDate.year
if (currentDate.month) == 1:
    month = "January"
elif (currentDate.month) == 2:
    month = "February"
elif (currentDate.month) == 3:
    month = "March"
elif (currentDate.month) == 4:
    month = "April"
elif (currentDate.month) == 5:
    month = "May"
elif (currentDate.month) == 6:
    month = "June"
elif (currentDate.month) == 7:
    month = "July"
elif (currentDate.month) == 8:
    month = "August"
elif (currentDate.month) == 9:
    month = "September"
elif (currentDate.month) == 10:
    month = "October"
elif (currentDate.month) == 11:
    month = "November"
elif (currentDate.month) == 12:
    month = "December"
if currentDate.day == 1:
    day = "1st"
elif currentDate.day == 2:
    day = "2nd"
elif currentDate.day == 3:
    day = "3rd"
elif currentDate.day == 4:
    day = "4th"
elif currentDate.day == 5:
    day = "5th"
elif currentDate.day == 6:
    day = "6th"
elif currentDate.day == 7:
    day = "7th"
elif currentDate.day == 8:
    day = "8th"
elif currentDate.day == 9:
    day = "9th"
elif currentDate.day == 10:
    day = "10th"
elif currentDate.day == 11:
    day = "11th"
elif currentDate.day == 12:
    day = "12th"
elif currentDate.day == 13:
    day = "13th"
elif currentDate.day == 14:
    day = "14th"
elif currentDate.day == 15:
    day = "15th"
elif currentDate.day == 16:
    day = "16th"
elif currentDate.day == 17:
    day = "17th"
elif currentDate.day == 18:
    day = "18th"
elif currentDate.day == 19:
    day = "19th"
elif currentDate.day == 20:
    day = "20th"
elif currentDate.day == 21:
    day = "21st"
elif currentDate.day == 22:
    day = "22nd"
elif currentDate.day == 23:
    day = "23rd"
elif currentDate.day == 24:
    day = "24th"
elif currentDate.day == 25:
    day = "25th"
elif currentDate.day == 26:
    day = "26th"
elif currentDate.day == 27:
    day = "27th"
elif currentDate.day == 28:
    day = "28th"
elif currentDate.day == 29:
    day = "29th"
elif currentDate.day == 30:
    day = "30th"
elif currentDate.day == 31:
    day = "31st"
colon = ":"
hour = currentDate.hour
minute = currentDate.minute
second = currentDate.second
print(year, colon, month, colon, day, colon, hour, colon, minute, colon, second)
