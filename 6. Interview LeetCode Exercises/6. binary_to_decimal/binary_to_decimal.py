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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    def binary_to_decimal(self):
        total = 0
        if self.head is None:
            return total
        else:
            binary_list = []
            current = self.head
            index = 0
            while current:
                binary_list.insert(index, current.value)
                index+=1
                current = current.next  
            while len(binary_list) < 8:
                binary_list.insert(0,0)
            binary_value = 128
            for element in binary_list:
                total = total + (element*binary_value)
                binary_value = binary_value/2
            return total

