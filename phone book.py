
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


                