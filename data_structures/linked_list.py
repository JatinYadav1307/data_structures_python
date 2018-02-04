from helper.simple_node import Node


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    @staticmethod
    def create_node(name, email, phone_number):
        return Node().set_data(name, email, phone_number).set_next_node(None)

    def insert_in_front(self, node):
        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.set_next_node(self.start)
            self.start = node

    def insert_in_end(self, node):
        if self.start is None:
            self.start = node
            self.end = node
        else:
            current_node = self.start

            while current_node is not self.end:
                current_node = current_node.get_next_node()

            current_node.set_next_node(node)
            self.end = node

    def delete_from_front(self):
        if self.start:
            if self.start is self.end:
                self.start = self.end = None
            else:
                self.start = self.start.get_next_node()

    def delete_from_end(self):
        if self.start:
            if self.start is self.end:
                self.start = self.end = None
            else:
                current_node = self.start

                while current_node.get_next_node() is not self.end:
                    current_node = current_node.get_next_node()

                current_node.set_next_node(None)
                self.end = current_node

    def get_list(self):
        current_node = self.start
        resultant_list = list()

        while current_node is not None:
            resultant_list.append(current_node.get_data())
            current_node = current_node.get_next_node()

        return resultant_list
