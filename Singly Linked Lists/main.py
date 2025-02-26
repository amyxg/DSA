"""
NOTE: 
Node class implements a list node with two data members, a data value and the next node in the list. 
If the node has no next node, the next data member is assigned with None, the Python term signifying the absence of a value.

LinkedList class implements the list data structure and contains two data members, head and tail, 
which are assigned to nodes once the list is populated.
Initially the list has no nodes, so both data members are initially assigned with None.

@amyxg
"""

from Node import Node
from LinkedList import LinkedList


num_list = LinkedList()

node_a = Node(11)
node_b = Node(22)
node_c = Node(33)
node_d = Node(45)
node_e = Node(66)
node_f = Node(79)

num_list.append(node_b)   # Add 22
num_list.append(node_c)   # Add 33, make the tail
num_list.append(node_e)   # Add 66, make the tail

num_list.prepend(node_a)  # Add 11, make the head

num_list.insert_after(node_c, node_d)  # Insert 33 after 45
num_list.insert_after(node_e, node_f)  # Insert 66 after tail (79)

# Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.remove_after(node_e)   # Remove the tail (79)
num_list.remove_after(None)     # Remove the head (11)


# Output final list
print('List after removing nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()
