from doubly_linked_list import DoublyList

my_list = DoublyList(3)
my_list.append(4)
my_list.pop()
my_list.prepend(2)
my_list.pop_first()
print(my_list.get(0))
my_list.set_value(0, 1)
my_list.insert(0, 2)

my_list.remove(1)
my_list.prepend(1)
my_list.append(3)
my_list.reverse()
my_list.print_list()
