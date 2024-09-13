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
    count_nodes = LinkedList.head
    count = 1

    while count_nodes is not None:
        count+=1
        count_nodes = count_nodes.next
    
    
    if k >= count:
        return None
    else:
        for _ in range(k+1):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            if fast is None or fast.next is None:
                return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

