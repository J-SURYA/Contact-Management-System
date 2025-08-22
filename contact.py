class Contact:
    def __init__(self,name,mail,phone):
        self.name = name
        self.mail = mail
        self.phone = phone

    def __str__(self):
        return f'{self.name},{self.mail},{self.phone}'
    
    def from_str(contact_str):
        name,mail,phone = contact_str.strip().split(",")
        return Contact(name,mail,phone)