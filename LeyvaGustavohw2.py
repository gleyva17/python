
print("Hello, welcome to Hopper's Computer Museum!")
print ("To determine your entrance fee, please enter the following")

print("Your Date of Birth (mm dd yyyy)")
line = input("Enter birth date: ")
print("Your birthdate is: ", line)

## prints the birthdate in one line, and also converts them to integers.
parts = line.split()
month = int(parts[0])
day = int(parts[1])
year = int(parts[2])

##imports current date from the computer
import time
today = time.strftime("%m/%d/%Y")
todayParts = today.split("/")
cMonth = int(todayParts[0])
cDay = int(todayParts[1])
cYear = int(todayParts[2])
print ("the current date is: ", cMonth, cDay, cYear)

age = cYear - year

if (month == cMonth and day > cDay):
    age = age - 1
elif (month > cMonth):
    age = age - 1
    
print('Your age is', age) 

coupon = input('Do you have a coupon(y/n)')

if age < 15:
    adminPrice = 5.0
elif age < 65:
    adminPrice = 9.0
else:
    adminPrice = 7.5

if coupon == 'y' or coupon == 'Y':
    adminPrice = adminPrice - 1.0
print("Admission price is: ${:.2f}".format(adminPrice))

## Created by Gustavo Leyva


