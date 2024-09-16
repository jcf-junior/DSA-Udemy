# This is a less efficient approach than 2 pointers because it traverses the list once to 
# find the middle point, using the count variable [O(n)], and traverses another half of the list
# to find the middle_node [O(n/2)]. So this comes to a total of O(3/2*n)
# A 2 pointer approach, would find the middle node in a single iteration, which is O(n).

def find_middle_node(self):
    count = 0
    find_count = self.head
    while find_count is not None:
        find_count = find_count.next
        count+=1
    if count%2==0:
        mid=count//2
        middle_node = self.head
        for _ in range(mid):
            middle_node = middle_node.next
        return middle_node
    else:
        mid = int(count/2)
        middle_node = self.head
        for _ in range(mid):
            middle_node = middle_node.next
        return middle_node
