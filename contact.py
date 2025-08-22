class Contact:
    def __init__(self,name,mail,phone):
        self.name = name
        self.mail = mail
        self.phone = phone

    def __str__(self):
        return f'Contact(name = {self.name},phone = {self.phone}, mail = {self.mail})'