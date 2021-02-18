class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def get(self, index):

        assert index >= 0

        item = self.head
        assert item is not None
        for _ in range(index):
            item = item.next
            assert item is not None

        return item.value

    def add(self, index, value):

        assert index >= 0

        new = Node(value)

        if index == 0:
            if self.head is not None:
                new.next = self.head
            self.head = new

        else:
            prev = self.head
            for _ in range(index-1):
                assert prev is not None
                prev = prev.next

            assert prev is not None

            new.next = prev.next
            prev.next = new

    def remove(self, index):

        assert index >= 0

        if index == 0:
            assert self.head is not None
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index - 1):
                assert prev is not None
                prev = prev.next

            assert prev is not None
            assert prev.next is not None
            prev.next = prev.next.next

    def __str__(self):
        array = []
        item = self.head
        while item is not None:
            array.append(item.value)
            item = item.next
        return array.__str__()
