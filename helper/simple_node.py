class Node:
    def __init__(self):
        self.name = None
        self.email = None
        self.phone_number = None
        self.next_node = None

    def set_data(self, name, email, phone_number):
        self.set_name(name)
        self.set_email(email)
        self.set_phone_number(phone_number)
        return self

    def get_data(self):
        return self.get_name(), self.get_email(), self.get_phone_number()

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node
        return self

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        return self

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        return self
