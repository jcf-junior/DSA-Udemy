class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
   
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

def find_kth_from_end(LinkedList, k):
    fast = LinkedList.head
    slow = LinkedList.head
    for _ in range(k):
        fast = fast.next
        if fast == None:
            return None
    if fast == LinkedList.tail:
        return LinkedList.head.value
    while fast is not None:
        slow = slow.next
        fast = fast.next    
        if fast == None:
            return slow.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

