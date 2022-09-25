class Node:

    # Constructor to create a new node
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List
class DoublyLinkedList:
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, Name, Age):
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(Name, Age)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    # Given a node as prev_node, insert a new node after
    # the given node
    def insertAfter(self, prev_node, Name, Age):

        # 1. Check if the given prev_node is None
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        # 2. allocate new node
        # 3. put in the data
        new_node = Node(Name, Age)

        # 4. Make net of new node as next of prev node
        new_node.next = prev_node.next

        # 5. Make prev_node as previous of new_node
        prev_node.next = new_node

        # 6. Make prev_node ass previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_nodes's next node
        if new_node.next:
            new_node.next.prev = new_node

    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def append(self, Name, Age):

        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(Name, Age)

        # 3. This new node is going to be the last node,
        # so make next of it as None
        # (It already is initialized as None)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last

        return

    def printList(self, node):

        print("\nTraversal in forward direction")
        while node:
            print(" {} {}".format(node.name, node.age))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print(" {} {}".format(last.name, last.age))
            last = last.prev


# Driver code


# Start with empty list
if __name__ == "__main__":
    llist = DoublyLinkedList()
    llist.append("Me",18)
    llist.append("Father", 48)
    llist.append("Mother", 46)
    llist.append("Grandpa", 70)
    llist.append("Grandma", 68)
    print("Created DLL is: ")
    llist.printList(llist.head)

# Bonus question:
#Q. Try to find a way to link the family members' doubly-linked list based on their relationship.
#A. We can link the family member nodes according to the age of the members in ascending and 
#   descending order for front traversal and reverse traversal respectively.
