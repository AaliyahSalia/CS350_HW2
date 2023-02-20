# Assuming that there are two linked lists with positive number type value in each node, 
# such as u= "Head->1->2->3->4->NULL" and v="Head->5->6->7->8->NULL", two 
# numbers 1234 & 5678 from the linked lists can be extracted respectively, and make 
# addition operation for two numbers, the result will be 6912(=1234+5678) . Find a 
# function/method to implement above operations and get such result "Head->6->9->1
# ->2->NULL" if calling function LL_add(u,v)  

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

    def LL_add(self, u, v):
        u_num = self.get_num(u)
        v_num = self.get_num(v)
        sum_num = u_num + v_num
        sum_list = self.get_list(sum_num)
        temp = self.head
        index = 0
        while temp:
            temp.data = sum_list[index]
            index += 1
            temp = temp.next

    def get_num(self, u):
        num = 0
        temp = u.head
        while temp:
            if temp.data.isnumeric():
                num = num * 10 + int(temp.data)
            temp = temp.next
        return num

    def get_list(self, num):
        num_list = []
        while num != 0:
            num_list.append(num % 10)
            num = num // 10
        num_list.reverse()
        return num_list

if __name__ == '__main__':
    u = LinkedList()
    u.head = Node('1')
    u.head.next = Node('2')
    u.head.next.next = Node('3')
    u.head.next.next.next = Node('4')
    v = LinkedList()
    v.head = Node('5')
    v.head.next = Node('6')
    v.head.next.next = Node('7')
    v.head.next.next.next = Node('8')
    u.LL_add(u, v)
    u.printList()

