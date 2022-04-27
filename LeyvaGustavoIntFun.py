
## Gustavo Leyva
## attempted extra credit, all 3 options attempted.
print("Welcome to Integer Fun!, please don't crash my code (: ")
option = " "
odds = 0
even = 0
num = 0
numero = 0
digit = 0
zeroes = 0

## here it starts by asking the user to enter an integer
num = int(input("Enter an integer to start with: "))
numero = num

##code to not accept negative input
if num < 0:
    print("invalid integer")
while option != "5" :
    ##  the loop continues until option "5" is selected.

    while option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
        print("\nPlease select from the following options: ")
        print("\n1. Enter a new number")
        print("2. Print the number of odd, even and zero digits in the integer ")
        print("3. Print the prime numbers between 2 and the integer")
        print("4. Print the sum of the digits of the integer ")
        print("5. Quit")
        option = input("\nYour choice --> ")
        

        if option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
            print("\nInvalid input - please try again\n")
        
    print("\nYou selected option ", option)



    ##  if option '5' has not been selected, clear 'option'...
    if option == "1":
        num = int(input("Enter the new number: "))
        even = 0
        odds = 0
        zeroes = 0
        option = "0"
        
##option 2
    if option == "2":
        while numero > 0:
            digit = numero %10
            numero = numero // 10
            if digit == 0:
                zeroes = zeroes + 1
            elif digit %2 == 0:
                even = even + 1
            else:
                odds = odds + 1
        print("Odds Evens Zero(s):", odds, even, zeroes)
        option = "0"

##option gets reset at the end of every line of code to show menu again
## code option 3 is here,prints out all the prime number
## between 2 and integer inputed.
    elif option == "3":
        for prime in range(2,num):
            if all(prime%i!=0 for i in range(2,prime)):
               print (prime)
        option = "0"

## option 4 code to add the digits of the integer         
    elif option == "4":
        s = 0
        while num:
            s += num % 10
            num //= 10
        print("The sum of the digits of the integer is", s)
        option = "0"
