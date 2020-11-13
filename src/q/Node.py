class Node:

    def __init__(self, contained_obj=None, next_obj=None):
        self.__contained_obj = contained_obj
        self.__next_obj = next_obj

    @property
    def value(self):
        return self.__contained_obj

    @property
    def next(self):
        return self.__next_obj

    @value.setter
    def value(self, new_obj):
        self.__contained_obj = new_obj

    @next.setter
    def next(self, new_obj):
        self.__next_obj = new_obj

    def is_last(self):
        return self.next is None

    def is_not_last(self):
        return not self.is_last()

    def __str__(self):
        return "({}, {})".format(self.value, self.next.value if self.next else None)

