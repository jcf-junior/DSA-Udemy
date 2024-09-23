class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self,x):
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current_node = self.head

        while current_node:
            if current_node.value < x:
                prev1.next = current_node
                prev1 = current_node
            else:
                prev2.next = current_node
                prev2 = current_node
            current_node = current_node.next
        
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next

#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    print("-----------------------")
    
# Run the test function
test_partition_list()
      