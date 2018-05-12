# Singly Linked List implementation

class Node:
    def __init__(self):
        self.data = 0
        self.nextNode = 0


class LinkedList:
    def __init__(self):
        self.head = 0
        self.size = 0

    def addNode(self,data):
        newNode = Node()
        newNode.next = self.head
        newNode.data = data
        self.head = newNode
        self.size = self.size +1


    def deleteNode(self):
        self.head = self.head.nextNode
        self.size = self.size - 1



#API
newList = LinkedList()
newList.addNode(2)
print(newList.head.data)
newList.deleteNode()
print(newList.head)