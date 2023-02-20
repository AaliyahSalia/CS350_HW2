# Given a linked list, write a program to check if there exists an internal linked loop or not. 
# For instance, as following, return value of function/method is_loopLL(a) is true, 
# otherwise false.
# Notice that there is ONLY one link to next in node structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    def is_loopLL(self):
        temp = self.head
        while temp:
            if temp.next == self.head:
                return True
            temp = temp.next
        return False

if __name__ == '__main__':
    a = LinkedList()
    a.head = Node('A')
    a.head.next = Node('B')
    a.head.next.next = Node('C')
    a.head.next.next.next = Node('D')
    a.head.next.next.next.next = Node('E')
    a.head.next.next.next.next.next = a.head
    print(a.is_loopLL())

