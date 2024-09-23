class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length == 0 or self.length == 1:
            return False
        else:  #self.length > 1
            
            pointer1 = self.head
            before = None
            pointer2 = self.head.next
            after = pointer2.next

            while pointer1 is not None:
                pointer2.prev = before
                pointer1.next = after
                pointer1.prev = pointer2
                pointer2.next = pointer1

                if before is not None:
                    before.next = pointer2
                if after is not None:
                    after.prev = pointer1

                if pointer1 == self.head:
                    self.head = pointer2

                before = pointer1
                pointer1 = after
                if pointer1 is None:
                    break
                pointer2 = pointer1.next
                if pointer2 is None:
                    break
                after = pointer2.next
            

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""