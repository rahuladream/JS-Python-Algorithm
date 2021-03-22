# Program to revers linked list

class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:

    # function to initialize head
    def __init__(self):
        self.head = None
    
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # function to insert a new node at the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node
    
    # function to print the linkedlist
    def prettyPrint(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(2)
    llist.push(4)
    llist.push(15)
    llist.push(18)

    print("Given linked list")
    llist.prettyPrint()
    llist.reverse()
    print("Reverse linked list")
    llist.prettyPrint()