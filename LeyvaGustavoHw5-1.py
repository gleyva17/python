## Gustavo Leyva, HW5
#List Array assignment 
##Extra credit attempted


##main functions where the choice made is called
def main():
    print("welcome to List Array (^-^)")
    scores = []
    choice = displayMenu()
    while choice != '6':
        if choice == '1':
            addNum(scores)
        elif choice == '2':
            getMean(scores)
        elif choice == '3':
            getMedian(scores)
        elif choice == '4':
            printList(scores)
        elif choice == '5':
            reverseList(scores)
        
        choice = displayMenu()
        
    print ("Thanks for using my code")


#____________________displays menu for user to choose from___________________
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4' \
          and myChoice != '5' and myChoice != '6':
        print ("""\n\nPlease choose
            1. Add a number to the list/array
            2. Display the mean
            3. Display the median
            4. Print the list/array to the screen
            5. Print the list/array in reverse order
            6. Quit""")
        myChoice = input("Enter option--> ")

        if myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4' \
           and myChoice != '5' and myChoice != '6':
            print ("Invalid option. Please select again")
        return myChoice


#_____________________________________________________________________    
## adds a new element to the scores list, while also making sure the input is in the correct form
def addNum(aList):
    while True:
        try:
            nNum = input("enter a positive integer, ")
            nNum = int(nNum)
            if nNum < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input... Please try again.")
    aList.append(nNum)
    print(aList)

#__________________calcs mean__________________________________________ 
def getMean(sList):
    sList.sort()
    total = 0
    for value in sList:
         total += value
         mean = total/len(sList)
         
    print("The mean is: {:.2f}".format(mean))

    
#__________________________________________________________________________
##sorts the list first then calculates the middle number(median)
def getMedian(aList):
    aList.sort()
    mid = len(aList)//2
    if len(aList) % 2 == 1:
        med= aList[mid]
    else:
        ave= aList[mid]+aList[mid-1]
        med= ave/2.0
    print("the median is: {:.2f}".format(med))
    
#________________________________________________________________________
## print the list in array order, one under the other. 
def printList(tList):
    tList.sort()
    print("Here are the values of the list")
    for value in tList:
        print(value)

#_________________________EXTRA CREDIT_________________________________
## prints the list sorted in reverse order,
def reverseList(pList):
    pList.sort(reverse=True)
    for val in pList:
        print(val)


main()
