#Name : Navodit Gupta
#SID : 21107082
#Branch : Mechanical
class Node:
      
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data 
        self.next = None
  
class CircularLinkedList:
      
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
  
    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
          
        ptr1.next = self.head
  
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head): #This condition establishes that the traversing
                                           #element(temp) has reached the first element
                temp = temp.next 
            temp.next = ptr1
  
        else:
            ptr1.next = ptr1 # For the first node
  
        self.head = ptr1 
  
    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print (temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break 
  

  
# Initialize list as empty
cllist = CircularLinkedList()

cllist.push(10)
cllist.push(20)
cllist.push(30)
cllist.push(40)
print ("Contents of circular Linked List")
cllist.printList()


"""
Q2. Practical applications of circular linked list.
A. practical applications of circular linked list-
-> Music/Video streaming: when a playlist is completed, it can go back to the start.
-> Multitasking: Change between apps
-> The browser cache which allows you to hit the BACK button
-> Undo functionality in Photoshop or Word
"""
