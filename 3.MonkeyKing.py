# Solve monkey king election question on the handout by circular linked list in a program
# Input 
# Enter total number of monkeys in a group: 5 
# Enter m value: 3 
#       Output 
# The king will be 3 
#       Input 
# Enter total number of monkeys in a group: 8 
# Enter m value: 5 
#       Output 
# The king will be 2 
# Notice that 1st monkey’s label should start with 0 as an index 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
        if current.data == key:
            prev.next = current.next

    def find_king(self, m):
        current = self.head
        while current.next != current:
            for i in range(m-1):
                current = current.next
            self.remove(current.data)
            current = current.next
        return current.data


if __name__ == '__main__':
    n = int(input("Enter total number of monkeys in a group: "))
    m = int(input("Enter m value: "))
    monkeys = CircularLinkedList()
    for i in range(n):
        monkeys.add(i)
    king = monkeys.find_king(m)
    print("The king will be", king)

    