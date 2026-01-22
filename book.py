contact = {}

FILE_NAME = "contacts.txt"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contact[name] = phone
    except FileNotFoundError:
        pass
def save_contacts():
    with open(FILE_NAME, "w") as file:
        for name, phone in contact.items():
            file.write(name + "," + phone + "\n")
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
load_contacts()
while True:
     choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact\n 4. Edit contact \n 5. Delete contact\n 6. Exit\n Enter your choice"))
     if choice == 1:
        name = input("enter the contact name")
        phone = input("enter the mobile number")
        contact[name] = phone
        save_contacts()
        print("Contact added successfully")
     elif choice ==2:
         search_name = input("enter the contact name")
         if search_name in contact:
             print(search_name,"'s contact number is ",contact[search_name])
         else:
             print("Name is not found in contact book")
     elif choice == 3:
         if not contact:
             print("empty contact book")
         else:
             display_contact()
     elif choice == 4:
         edit_contact = input("Enter the contact to be edited")
         if edit_contact in contact:
             phone = input("enter mobile number")
             contact[edit_contact]=phone
             save_contacts()
             print("contact updated")
             display_contact()
         else:
             print("Name is not found in contact book")
     elif choice == 5:
         del_contact = input("Enter the contact to be deleted")
         if del_contact in contact:
             confirm = input("Do you want to delete this contact (y/n)? ")
             if confirm =='y' or confirm =='Y':
                 contact.pop(del_contact)
                 save_contacts()
                 print("Contact deleted")
         else:
             print("Name is not found in contact book")
     else:
         break
             
         
             
