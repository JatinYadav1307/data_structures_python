from data_structures.linked_list import LinkedList
from faker import Faker

linked_list = LinkedList()
faker = Faker()

for _ in range(0, 10):
    node = LinkedList.create_node(faker.name(), faker.email(), faker.phone_number())
    linked_list.insert_in_end(node)

for item in linked_list.get_list():
    print(item)

for _ in range(0, 9):
    linked_list.delete_from_end()

print("\n\n")

for item in linked_list.get_list():
    print(item)
