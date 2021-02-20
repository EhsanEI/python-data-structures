import numpy as np


class MinHeap():

    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

        ind = len(self.array) - 1
        while (ind-1)//2 >= 0 and self.array[(ind-1)//2] > self.array[ind]:
            temp = self.array[(ind-1)//2]
            self.array[(ind-1)//2] = self.array[ind]
            self.array[ind] = temp

            ind = (ind-1)//2

    def pop(self):
        assert len(self.array) > 0

        if len(self.array) == 1:
            return self.array.pop()
        else:
            min_value = self.array[0]
            self.array[0] = self.array.pop()

            self._bubble_down(0)
            return min_value

    def _bubble_down(self, ind):
        children = self.array[ind*2+1:ind*2+3]
        if len(children) > 0:
            min_child_ind = ind*2+1 + np.argmin(children)

            if self.array[min_child_ind] < self.array[ind]:
                temp = self.array[min_child_ind]
                self.array[min_child_ind] = self.array[ind]
                self.array[ind] = temp

                self._bubble_down(min_child_ind)

    def peek(self):
        return self.root

    def __str__(self):
        return self.array.__str__()
