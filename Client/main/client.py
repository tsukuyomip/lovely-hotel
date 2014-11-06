# coding: utf-8

class Client:
    def __init__(self, name=None, email=None, address=None):
        self.name = name
        self.email = email
        self.address = address

    def has_name(self, name):
        return self.name == name

    def has_email(self, email):
        return self.email == email

    def has_address(self, address):
        return self.address == address
