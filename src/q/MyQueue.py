from q.Node import Node


class MyQueue:

    def __init__(self):
        self.__head = Node()

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    def add(self, obj):
        self.head = Node(obj, self.head)

    def remove(self):
        self.__rm_last_val()

    def to_list(self):
        return MyQueue.__to_list(self.head)

    # slow but with no memory leaks
    def clear(self):
        while self.head.is_not_last():
            self.remove()

        self.clear_fast()

    def clear_fast(self):
        self.head = Node()

    def __rm_last_val(self):
        current_val = self.head

        if current_val.is_last():
            self.head = Node()
            return

        while current_val.next.is_not_last():
            current_val = current_val.next

        current_val.next = None

    @staticmethod
    def __to_list(node, acc=[]):
        if node.next is None:
            return acc

        return MyQueue.__to_list(node.next, acc + [node.value])
