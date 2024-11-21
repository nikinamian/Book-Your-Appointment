#Book An Appointment

import calendar
print("Hello, Welcome to Soft Dental & Orthodontics!")
print()
print("Let's schedule your next appointment")
print()


year = int(input("Enter the year: "))
while year<2024:
    print("Please enter a future/current year")
    year = int(input("Enter the year: "))


mon = int(input("Enter the month (1-12): "))
while mon>12:
    print("Please enter a valid month (1-12)")
    mon = int(input("Enter the month (1-12): "))


print("Sounds great! Here is the calendar.")
print()
print (calendar.month(year,mon))
print()
print("Now let's book the appointment.")
print()

day = int(input("Please enter the day you would like: "))
if day<1 or day>31:
    print("Please enter a valid day (1-31)")
    day = int(input("Please enter the day you would like: "))

#get input for time of day and hour of appointment
timeOfDay = input("Do you want to come in the morning or afternoon? Enter m for morning, a for afternoon, n for noon: ").strip()

if timeOfDay.upper() == "N":
    hour = "12"
    print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"pm")

elif timeOfDay.upper() == "M":
   hour = int(input("Would you like 10 or 11am: "))
   if hour<10 or hour>11:
       print("Please pick a valid morning time")
       hour = int(input("Would you like 10 or 11am: "))
   print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"am")

       
elif timeOfDay.upper() == "A":
   hour = int(input("What time between 12pm and 7pm would you like to come in: "))
   if hour<1 or hour>7:
       print("Please pick a valid morning time")
       hour = int(input("What time between 12pm and 7pm would you like to come in: "))
   print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"pm")


       

#print("Great! You're appointment has been booked.")

#clairfy am/pm for appointment
if timeOfDay == "M":
    print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"am")
if timeOfDay == "N":
    print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"pm")
if timeOfDay == "A":
    print("You're appointment is for",mon,"-",day,"-",year,"at",hour,"pm")
print()
print("Great! You're appointment has been booked. See you then!")

