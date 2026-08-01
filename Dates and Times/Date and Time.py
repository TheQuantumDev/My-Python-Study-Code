import datetime

date = datetime.date(2026, 1, 1)
print(f"Custom date is {date}")

today = datetime.date.today()
print(f"Today's date is {today}")

time = datetime.time(5, 10, 22)
print(f"Custom time is {time}")

timeNow = datetime.datetime.now()
print(f"Time and date now is {timeNow}")

# Formatting the time with the string format time method(strftime())
timeNow = timeNow.strftime("%d/%m/%Y and the time is %H:%M:%S")
print(f"Properly formatted date and time now is {timeNow}")

# Comparing two dates
targetDatetime = datetime.datetime(2030, 11, 17, 12, 0, 0)
currentDatetime = datetime.datetime.now()

if targetDatetime < currentDatetime:
    print("The target date has been passed")
else:
    print("The target date has not been passed")