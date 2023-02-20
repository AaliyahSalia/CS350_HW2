# Given two singly linked lists with char type value node, like a-zA-Z
# l= "Head->G->O->O->D->NULL", and m ="Head->G->o->O->g->L->E->NULL", 
# Find the common char values and form a new linked list "Head->G->O->NULL" 
# through a function/method called commElem(l, m). 

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

    def commElem(self, l, m):
        l_char_list = []
        m_char_list = []
        temp = l.head
        while temp:
            if temp.data.isalpha():
                l_char_list.append(temp.data)
            temp = temp.next
        temp = m.head
        while temp:
            if temp.data.isalpha():
                m_char_list.append(temp.data)
            temp = temp.next
        comm_char_list = list(set(l_char_list) & set(m_char_list))
        comm_char_list.sort()
        temp = self.head
        index = 0
        while temp:
            if temp.data.isalpha():
                temp.data = comm_char_list[index]
                index += 1
            temp = temp.next

if __name__ == '__main__':
    l = LinkedList()
    l.head = Node('G')
    l.head.next = Node('O')
    l.head.next.next = Node('O')
    l.head.next.next.next = Node('D')
    m = LinkedList()
    m.head = Node('G')
    m.head.next = Node('o')
    m.head.next.next = Node('O')
    m.head.next.next.next = Node('g')
    m.head.next.next.next.next = Node('L')
    m.head.next.next.next.next.next = Node('E')
    comm = LinkedList()
    comm.head = Node('G')
    comm.head.next = Node('O')
    comm.commElem(l, m)
    comm.printList()

    