class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Linkedlist():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def view(self):
        x = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            x.append(cur.data)
        print(x)

my_list = Linkedlist()
my_list.append(1)
my_list.append(8)
my_list.view()

