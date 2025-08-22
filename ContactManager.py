from contact import Contact
class ContactManager:
    def __init__(self,filename='contacts.txt'):
        self.filename=filename
        self.contacts = self.load_contacts()
    def load_contacts(self):
        with open(self.filename,'r+') as f:
            return f.readlines()
    def save_contacts(self):
        with open(self.filename,'w+') as f:
            f.writelines(self.contacts)
    def addContact(self,contact):
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact Added Successfully!!")

    def deleteContact(self,name):
        pass

    def searchContact(self,name):
        pass

    def displayContact(self):
        pass

    def updateContact(self):
        pass

        