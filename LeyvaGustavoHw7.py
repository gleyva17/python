#Gustavo Leyva
#Assignment 7, Phone Book
##when I created this i had this file and the entries.txt file in my desktop.
## EXTRA CREDIT ATTEMPTED

#_______________________________________
def main():
    print("welcome to the Phone Book lookup")
    first_Name = [] #empty list to add the info from file
    lastName = []
    phoneNum = []

#_______________________________________
    myFile = "entries.txt"
    fileInput = open(myFile, "r") #opens for read only
    count = 0       #use a count to know what line is on to add to the correct list
    
    for string in fileInput:
        string = string.strip()
        string = string.lower()
        myNum = count % 3
        if myNum == 0:
            lastName.append(string) #last name added to LastName list.
        elif myNum == 1:
            first_Name.append(string)#first names added to a list
        elif myNum == 2:
            phoneNum.append(string)#phone numbers added to a list
        count = count + 1
    
#_________________________________________  
    choice = displayMenu()
    while choice != '4':
        if choice == '1':
            last_Look(lastName, first_Name, phoneNum)
        elif choice == '2':
            first_look(lastName, first_Name, phoneNum)
        elif choice == '3':
            phone_look(lastName, first_Name, phoneNum)
            
        choice = displayMenu()

#____________________displays menu for user to choose from___________________
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4':
        print ("""\n\nPlease choose
            1. Look up by Last Name
            2. Look up by First Name
            3. Look up by Phone Number
            4. Quit """)
        myChoice = input("Enter option--> ")

        if myChoice != '1' and myChoice != '2' and myChoice != '3' and myChoice != '4':
           
            print ("Invalid option. Please select again")
        return myChoice

#_____________________________________________________________
def last_Look(l_Name, f_Name, p_Number):
    last = input("Enter last Name to search by: ")
    last = last.strip()      #strips off the space/carriage return 
    last = last.lower()       #lower case letters 

    position = 0

    if last in l_Name:
        while True:
#prints out the information if the input is found
            try:
                position = l_Name.index(last, position)  
                print(l_Name[position].title())
                print(f_Name[position].title())
                print(p_Number[position])
                position = position + 1  #will move onto the next one and only print
                                        #if it matches the search
            except:
                break
    else: #if input not in file it prints out a message to user
        print(last, "not found in phone book. Please try another search.")
    
#__________________________________________________________________
def first_look(l_Name, f_Name, p_Number):
    first = input("Enter First Name to search by: ")
    first = first.strip()
    first = first.lower()

    position = 0
#prints out the information if the input is found
    if first in f_Name:
        while True:

            try:
                position = f_Name.index(first, position)  
                print(l_Name[position].title())
                print(f_Name[position].title())
                print(p_Number[position])
                position = position + 1  
            except:
                break
    else:
        print(first, "not found in phone book. Please try another search.")

#_________________________________________________________________
def phone_look(last_name, fname, p_Number):
    p = input("Enter Phone Number to search by: ")
    p = p.strip()
##    phone = phone.lower()

    position = 0
#prints out the information if the input is found
    if p in p_Number:
        while True:

            try:
                position = p_Number.index(p, position)  
                print(last_name[position].title())
                print(fname[position].title())
                print(p_Number[position])
                position = position + 1  
            except:
                break
    else:
        print(p, "not found in phone book. Please try another search.")
    
   
main()
