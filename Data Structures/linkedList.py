# Node class
class Node:
    # define node object
    def __init__(self, data):
        self.data = data # data
        self.next = None  # pointer to next node

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # add node the front
    def pushFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # add after a given node
    def pushMiddle(self, prev_node, new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


# execute code here
if __name__ == '__main__':
    # singly linked list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
