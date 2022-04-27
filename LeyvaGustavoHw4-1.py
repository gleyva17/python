## Gustavo Leyva, Hw4

## main function just calls for whatever option is made
def main():
    choice = displayMenu()
    while choice != '6':
        if choice == '1':
            getMeters()
        elif choice == '2':
            getFeet()
        elif choice == '3':
            getCelsius()
        elif choice == '4':
            getFahrenheit()
        elif choice == '5':
            rePhrase()
        
        choice = displayMenu()

    print ("Thanks for playing!")
    
##this will display the menu for the user to chose from
## after a selection is made the choice will be returned to the main function so the next action will execute
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4' \
          and myChoice != '5' and myChoice != '6':
        print ("""\n\nPlease choose
            1. Convert Feet to meters
            2. Convert meters to feet
            3. Convert Fahrenheit to Celsius
            4. Convert Celsius to Fahrenheit
            5. Display a phrase or number backawards
            6. Quit""")
        myChoice = input("Enter option--> ")

        if myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4' \
           and myChoice != '5' and myChoice != '6':
            print ("Invalid option. Please select again")
        return myChoice

##simply converts user input to meters 
def getMeters():
    theFeet = int(input("\n\nEnter the value in feet: "))
    print("\n\n The value in meters is: {:.2f}".format(theFeet / 3.28))

## converts user input to feet  
def getFeet():
    theMeters = int(input("\nEnter value in meter: "))
    print("\n\n The value in feet is: {:.2f}".format(theMeters * 3.28)) 

## calculates value of degrees in celsius
def getCelsius():
    theFahrenheit = input("Enter value in Fahrenheit: ")
    theFahrenheit = float(theFahrenheit)
    celsius =((theFahrenheit - 32) * 5/9)
    print("\n\n The value in Celsius is: {:.2f}".format(celsius))

## converts the value from celsius to fahrenheit
def getFahrenheit():
    theCelsius = input("Enter value in Celsius: ")
    theCelsius = float(theCelsius)
    fahrenheit = ((theCelsius * 1.8) + 32)
    print("\n\n The value in Fahrenheit is: {:.2f}".format(fahrenheit))

## will print the input backwards
def rePhrase():
    phrase = input("enter a phrase or number: ")
    backwards = phrase[::-1]
    print(backwards)


main()
