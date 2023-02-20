# Implement two-polynomial multiplication operation (convolution) by a program 
# conv_LL(l, m)
# e.g.  𝑙= 1𝑥0 +           2𝑥2 +3𝑥3 +           4𝑥5
#            𝑚= 5𝑥0 +6𝑥1 +           7𝑥3 + 8𝑥4
  
#       𝑙∗𝑚= 5𝑥0 +6𝑥1 +10𝑥2  + 34𝑥3 +26𝑥4 +34𝑥5 + 61𝑥6  +  24𝑥7 + 28𝑥8 + 32 𝑥9

class Node:
    def __init__(self, coeff=0, exp=0):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def printList(self):
        current = self.head
        while current is not None:
            print(current.coeff, 'x^', current.exp, end='')
            current = current.next
            if current is not None:
                print(' + ', end='')
        print()

    def convolution(self, other):
        result = LinkedList()
        current_l = self.head
        while current_l is not None:
            current_m = other.head
            while current_m is not None:
                coeff = current_l.coeff * current_m.coeff
                exp = current_l.exp + current_m.exp
                node = result.head
                prev = None
                while node is not None and node.exp > exp:
                    prev = node
                    node = node.next
                if node is not None and node.exp == exp:
                    node.coeff += coeff
                else:
                    new_node = Node(coeff, exp)
                    if prev is None:
                        result.head = new_node
                    else:
                        prev.next = new_node
                    new_node.next = node
                current_m = current_m.next
            current_l = current_l.next
        return result

if __name__ == '__main__':
    l = LinkedList()
    l.add(1, 0)
    l.add(2, 2)
    l.add(3, 3)
    l.add(4, 5)
    m = LinkedList()
    m.add(5, 0)
    m.add(6, 1)
    m.add(7, 3)
    m.add(8, 4)
    l.printList()
    m.printList()
    result = l.convolution(m)
    result.printList()
