## Assignment 1, Age at Graduation

## Gustavo Leyva Morales

print ("Welcome to the Age of graduation calculator!")

print ("Created by Gustavo Leyva Morales")

bYear = input("Birth year: ")

bYear = int(bYear)

bMonth = input("Birth month: ")

bDay = input("Birth day: ")

## Get the graduation Date...

gYear = input("Graduation year: ")

gYear = int(gYear)
            
gMonth = input("Graduation month: ")

gDay = input("Graduation day: ")

age = gYear - bYear

if (bMonth == gMonth and bDay > gday):
    age = age - 1
print (age) 



