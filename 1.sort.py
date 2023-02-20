#Write a function/method to sort a given linked list with char type node from a-zA-Z. 
#For example, ls = "Head->D->A->C->A->G->NULL", the new linked list should be 
#"Head->A->A->C->D->G->NULL" by calling function srt_LL(ls)

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

    def srt_LL(self):
        char_list = []
        temp = self.head
        while temp:
            if temp.data.isalpha():
                char_list.append(temp.data)
            temp = temp.next
        char_list.sort()
        temp = self.head
        index = 0
        while temp:
            if temp.data.isalpha():
                temp.data = char_list[index]
                index += 1
            temp = temp.next

if __name__ == '__main__':
    ls = LinkedList()
    ls.head = Node('D')
    ls.head.next = Node('A')
    ls.head.next.next = Node('C')
    ls.head.next.next.next = Node('A')
    ls.head.next.next.next.next = Node('G')
    ls.srt_LL()
    ls.printList()
