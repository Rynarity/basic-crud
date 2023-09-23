class Student:
    def __init__(self, full_name, age, gender, email_address):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.email_address = email_address

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_email_address(self):
        return self.email_address
