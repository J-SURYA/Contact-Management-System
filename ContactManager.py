from contact import Contact
class ContactManager:
    def __init__(self,filename = 'contacts.txt'):
        self.filename=filename
        self.contacts = self.load_contacts()

    def __del__(self):
        self.save_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                return [line for line in f.readlines()]
        except FileNotFoundError:
            return []
        
    def save_contacts(self):
        with open(self.filename,'w+') as f:
            f.writelines(line + "\n" for line in self.contacts)

    def addContact(self,contact):
        index = self.searchContact(contact.name)
        if index >= 0:
            print("Contact already exists.")
            return
        self.contacts.append(str(contact))
        self.save_contacts()
        print("Contact Added Successfully!!")

    def deleteContact(self,name):
        index = self.searchContact(name)
        if(index == -1):
            return
        if index >= 0:
            self.contacts.pop(index)
            self.save_contacts()
            print("Above contact deleted successfully.")
        else:
            print("Contact doesn't exists.")

    def searchContact(self,name):
        n = len(self.contacts)
        if(len(self.contacts) == 0):
            print("Your contact list is empty!")
            return -1
        i = 0
        for contact in self.contacts:
            if name == contact.split(',')[0]:
                print(contact.split(','))
                return i 
            i+=1
        return -2

    def displayContacts(self):
        if(len(self.contacts) == 0):
            print("Your contact list is empty!")
            return
        for contact in self.contacts:
            print(contact.split(','))

    def updateContact(self,name):
        i = self.searchContact(name)
        if(i == -1):
            return
        if(i != -2):
            ct = list(map(str,self.contacts[i].split(',')))
            if(ct[0] == name):
                print("Please enter the details of new contact:")
                newPhone = str(input("Phone :").strip())
                newMail = str(input("Mail :").strip())
                newContact = Contact(name,newMail,newPhone)
                self.contacts.pop(i)
                self.contacts.append(str(newContact))
                self.save_contacts()
                print("Contact updated Successfully")
        else:
            print("Given contact doesn't exist.")

        
