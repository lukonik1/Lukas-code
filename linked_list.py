class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linkedlist():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def lenght(self):
        l = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            l += 1
        return l

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= self.lenght():
            print ('ERROR')
            return None
        cur = self.head
        cur_inx = 0
        while True:
            cur = cur.next
            if cur_inx == index:
                return cur.data
            cur_inx += 1

    def erase(self, index):
        if index >= self.lenght():
            print ('ERROR')
            return
        cur = self.head
        cur_inx = 0
        while True:
            last_node = cur
            cur = cur.next
            if cur_inx == index:
                last_node.next = cur.next
                return None
            cur_inx += 1
    def append_at_index(self,data,index):
        if index >= self.lenght():
            print("ERROR")
            return
        new_node = Node(data)
        cur_inx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_inx == index:
                if cur.next != None:
                    new_node.next = cur.next
                cur.next = new_node
                return None
            cur_inx += 1

    def append_at_start(self,data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            return None
        new_node.next = self.head.next
        self.head.next = new_node
        return None

my_list = Linkedlist()


my_list.display()

my_list.append_at_start(5)

my_list.display()
