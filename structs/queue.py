class LIFO:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return self.stack.__str__()


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class FIFO:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        new = QueueNode(value)

        if self.last is None:
            assert self.first is None
            self.first = new
        else:
            self.last.next = new
        self.last = new

    def pop(self):
        assert self.first is not None
        first = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return first.value

    def peek(self):
        assert self.first is not None
        return self.first.value

    def __str__(self):
        array = []
        item = self.first
        while item is not None:
            array.append(item.value)
            item = item.next
        return array.__str__()
