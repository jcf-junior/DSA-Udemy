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
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse_between(self,start_index,end_index):
        if self.length == 0 or self.length == 1:
            return None
        else:
            current = self.head
            idx = 0 # Vai guardar o valor do índice do current, para poder comparar com os indices start e end. 
            first_reversed_node = None
            node_before_reversal = None
            prev_node = None
            

            while current is not None:
                next_node = current.next
                if idx == start_index - 1:
                    node_before_reversal = current  # Nó antes da secção a inverter
                if idx == start_index:
                    first_reversed_node = current  # Primeiro nó da secção a inverter
                if start_index <= idx <= end_index:
                    # Durante a inversão, atualiza os ponteiros
                    current.next = prev_node
                    prev_node = current
                if idx == end_index:
                    # Quando alcançamos o final da secção a inverter
                    if node_before_reversal is not None:
                        node_before_reversal.next = current  # Conecta o nó antes da secção ao último nó invertido
                    else:
                        self.head = current

                    first_reversed_node.next = next_node  # Conecta o primeiro nó da secção ao nó após a inversão
                    
                idx += 1
                current = next_node  # Atualiza o current para o próximo nó (já guardado)
                


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(0, 2)
print("Reversed sublist (0, 2): ")
linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
