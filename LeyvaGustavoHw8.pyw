##Gustavo Leyva
## tkinter PhoneBook, Assignemnt hw 8
## added a working scrollbar in the result textbx


from tkinter import *


##  'default' responds to the 'enter keypress' event...
def default(event):
  lookUp()

def lookUp():
  # Clear the listbox...
  listbox.delete(0, END)

  # Get the option button value...
  option = v.get()

  # Lookup by option chosen...
  if option == 1:
      getNames(fName)
  elif option == 2:
      getNames(lName)
  else:
      getNames(phone)


def getNames(theList):
  # Get the name/number to lookup...
  target = s.get()
  target = target.strip().lower()

  position = 0   # Starting position for the search...
  if target in theList:
      while True:
          try:
              position = theList.index(target, position)  # Will eventually raise an exception
              entry = fName[position].title() + " " + lName[position].title() + " " + phone[position]
              listbox.insert(END, entry)

              position = position + 1  # Resume search at next position...
          except:
              break
  else:         
      listbox.insert(END, "Search not in Phone Book...")

##  End program...
def quit():
  root.destroy()    



def loadLists():
  count = 0
   
  ##  Get the names and phone numbers..
  try:
      fileInput = open("entries.txt", "r")

      for myString in fileInput:
          myString = myString.strip()
          myString = myString.lower()
          myNum = count % 3
          
          if myNum == 0:
              lName.append(myString)
          elif myNum == 1:
              fName.append(myString)
          elif myNum == 2:
              phone.append(myString)
          count = count + 1
          
      fileInput.close()
  except:
      pass

##  Lists for the names and number of contacts..
lName = []
fName = []
phone = []
loadLists()

##  Creating the main form
root = Tk()
root.geometry("500x300+320+200")
root.title("CSCD110 - Introduction to Programming")
root.bind('<Return>', default)

##  Title frame...
fraTitle = Frame(root, height=2, bd=1)
lbl1 = Label(fraTitle, text="Phone Book Application")
lbl1.config(font=(30))
lbl1.pack()

fraTitle.pack(fill=X, padx=5, pady=1)

##  Main frame...
fraMain = Frame(root, height=1, bd=1)

##  Option buttons...
v = IntVar()
optFName = Radiobutton(fraMain, text="First Name", variable=v, value=1).pack(pady=0, anchor=W)
optLName = Radiobutton(fraMain, text="Last Name", variable=v, value=2).pack(pady=0, anchor=W)
optPhone = Radiobutton(fraMain, text="Phone Number", variable=v, value=3).pack(pady=0, anchor=W)
v.set(1)

##  Entry text box...
s = StringVar()
txtValue = Entry(fraMain, textvariable=s).pack(fill=X, padx=5, pady=5, anchor=W)

##  results list box...Added a scrollbar in the result text box
listbox = Listbox(fraMain, height=5)
listbox.pack(fill=X, padx=5, pady=5, anchor=W)
scrollbar = Scrollbar(listbox, command=listbox.yview)
scrollbar.pack( side = RIGHT, fill=Y )


## Search button
btnLookUp = Button(fraMain, width=10, text="  Search  ", command=lookUp).pack(padx=5, pady=5, anchor=SE)

##  quit button
btnQuit = Button(fraMain, width=10, text="   Quit   ", command=quit).pack(padx=5, pady=5, anchor=SE)

##  Pack the main frame into the root...
fraMain.pack(fill=X, padx=5, pady=1)

mainloop()




