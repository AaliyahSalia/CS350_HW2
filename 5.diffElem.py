# Write a function diffElem_LL(l, m) as similar as above, but to exact all char values, 
# which are NOT common ones, and link them together, such as 
# "Head->D->o->g->L->E->NULL",   

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

    def diffElem_LL(self, l, m):
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
        diff_char_list = list(set(l_char_list) ^ set(m_char_list))
        diff_char_list.sort()
        temp = self.head
        index = 0
        while temp:
            if temp.data.isalpha():
                temp.data = diff_char_list[index]
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
    diff = LinkedList()
    diff.head = Node('D')
    diff.head.next = Node('o')
    diff.head.next.next = Node('g')
    diff.head.next.next.next = Node('L')
    diff.head.next.next.next.next = Node('E')
    diff.diffElem_LL(l, m)
    diff.printList()

    