
import sys
def initial_phonebook():
    rol,cols =int(input("please enter initial number of contacts" )),5
    phonebook=[]
    print(phone_book)
    for i in range (rows):
        print("\n enter contact %d details in the following order ")(ONLY):"%(I+1))"
        print("NOTE:*indicates mandatoryfields")
        print:("...................................................................")
     temp=[]
    for j in range(cols):
        if j ==0:
            temp append(str(input("Enter name: ")))
            if temp[j] == '' or temp[j] == ' ':
                sys.exit(
                    "Name is mandatory. Process exiting due to blank field...")
                if j == 1:
                    temp.append(str(input("Enter phone number: ")))
                if j == 2:
                    temp.append(str(input("Enter email: ")))
                    temp[j] = None
                if j == 3:
                    temp.append(str(input("date of birth(dd/mm/yy): ")))
                    if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                 if j == 4:
                        temp.append(str(input("Enter  family category(family/friends/work/others): ")))
                    if temp[j] == '' or temp[j] == ' ':
                            temp[j] = None
                            phonebook.append(temp)
    return phonebook
 def menu():
     print ("t/t/tSMARTPHONE DIRECTORY,flush=false")
     print("/t you can now perform the following operations on this phone book/n")

     print("1.add new contact")
     print("2.remove all existing contacts")
     print("3.delete all contacts")
     print("4.search for a contact")
     print("5.display all contacts")
     print("6.exit phone book")
     choice= int(input("please enter your choice:"))
      return choice
def add_contact(phonebook):
    dip=[]
    for i in range(len(pb[0])): 
         	if i == 0: 
			dip.append(str(input("Enter name: "))) 
		if i == 1: 
            dip.append(str(input("Enter phone number: ")))
        if i == 2:
            dip.append(str(input("enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(str(input("Enter family category(family/friends/work/others): ")))
    phonebook.append(dip)
     return phonebook
def remove_ existing (phone book):
   query = str(input("Enter name of contact to be removed: "))
   temp = 0


            