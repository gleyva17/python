#________Gustavo Leyva________________
#________HW6-Sieve of Eratosthenes____


def main():
    pList = []
    choice = displayMenu()
    while choice != '3':
        if choice == '1':
            pList=getPrime(pList)
        elif choice == '2':
            listPrint(pList)

        choice = displayMenu()

    print("Thanks for playing!")

#__________________________________________________________________
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' and myChoice != '3':
        print ("""\n\nPlease choose
            1. Create a list of primes from 2 to n 
            2. Display the prime numbers
            3. Quit """)
        
        myChoice = input("Enter option--> ")

        if myChoice != '1' and myChoice != '2' and myChoice != '3':
            print ("Invalid option. Please select again")
        return myChoice

    
#_________calculates primes using a for-in-range_____________________
def getPrime(pList):
##    lim=int(input("Find primes up to what number?"))
    while True:
        try:  #error checking
            lim = input("Find primes up to what number?")
            lim = int(lim)
            if lim < 2 or lim == 2:
                raise ValueError
            break
        except ValueError:
            print("Invalid input... Please try again.")
    primeList=[]
    for x in range(2,lim+1): #adds one to make the lim correct
        isPrime=True
        for y in range(2,int(x**0.5)+1) :
            if x%y==0:
                isPrime=False 
                break
        if isPrime:
            primeList.append(x) #only prime numbers added to list
    return(primeList)

#___________print one number at a time_____________________    
def listPrint(plist):
    for val in plist:
        print(val)
    

main()
