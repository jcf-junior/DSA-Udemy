class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def reverse_string(input):
    my_stack = Stack()
    for i in input:
        my_stack.push(i)
    reverse_string = ''
    for i in range(my_stack.size()):
        reverse_string += my_stack.pop()

    return reverse_string



my_string = 'hello'

print(reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
