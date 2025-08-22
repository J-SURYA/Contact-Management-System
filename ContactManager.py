from contact import Contact
class ContactManager:
    def __init__(self,filename='contacts.txt'):
        self.filename=filename
        self.contacts = self.load_contacts()
    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                return [line for line in f.readlines()]
        except FileNotFoundError:
            return []
    def save_contacts(self):
        with open(self.filename,'w+') as f:
            f.writelines(self.contacts)
    def addContact(self,contact):
        self.contacts.append(str(contact))
        self.save_contacts()
        print("Contact Added Successfully!!")

    def deleteContact(self,name):
        index = self.searchContact(name)
        if index != -1:
            self.contacts.pop(index)
            print("Contact deleted successfully.")
        else:
            print("no contacts present in this name")

    def searchContact(self,name):
        n = len(self.contacts)
        if(len(self.contacts) == 0):
            print("Your contact list is empty!")
            return -1
        i = 0
        for contact in self.contacts:
            if name in contact.split(',')[0]:
                print(contact.split(','))
                return i 
            i+=1
        return -2

    def displayContacts(self):
        for contact in self.contacts:
            print(contact.strip())
        if(len(self.contacts) == 0):
            print("Your contact list is empty!")

    def updateContact(self,name):
        i = self.searchContact(name)
        if(i == -1):
            return
        if(i != -2):
            ct = list(map(str,self.contacts[i].split(',')))
            if(ct[0] == name):
                print("Please enter the details of new contact:")
                newPhone = str(input("Phone :"))
                newMail = str(input("Mail :"))
                newContact = Contact(name,newMail,newPhone)
                self.contacts.pop(i)
                self.addContact(newContact)
                print("Updated Successfully")
        else:
            print("Given contact doesn't exist.")

        
