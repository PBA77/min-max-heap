from random import randint
from statistics import median


def _order_p(tree, n, fun):
    np = n >> 1
    element = tree[n]
    parent = tree[np]
    if fun(element, parent):
        tree[n], tree[np] = parent, element
        return True
    return False

def _put(tree, value, fun):
    tree.append(value)
    tree[0] += 1
    index = tree[0]
    while (index > 1) and _order_p(tree, index, fun): index >>= 1


def _pop(tree, fun):
    root = tree[1]
    size = tree[0]
    tree[1] = tree[size]
    tree[0] -= 1
    del tree[-1]
    index = 1
    while index < (size << 1):
        left = index << 1
        right = left + 1
        base = index
        if left < size and fun(tree[index], tree[left]):
            index = left
        if right < size and fun(tree[index], tree[right]):
            index = right
        if index != base:
            tree[base], tree[index] = tree[index], tree[base]
        else:
            break

    return root


lmin = lambda a, b: a < b
lmax = lambda a, b: a > b

class MinMaxHeap:

    def __init__(self):
        self.max_heap = [0]
        self.min_heap = [0]


    def clear(self):
        self.__init__()

    def getMedian(self):
        min_n, max_n = self.min_heap[0], self.max_heap[0]

        if min_n == 0 and max_n == 0:
            return None
        elif min_n == 0:
            return self.max_heap[1]
        elif max_n == 0:
            return self.min_heap[1]
        else:
            med_h, med_l = self.min_heap[1], self.max_heap[1]
            if min_n == max_n:
                return (med_h + med_l) / 2
            elif min_n > max_n:
                return med_h
            else:
                return med_l

    def put(self, number):
        min_n, max_n = self.min_heap[0], self.max_heap[0]

        if min_n == 0 and max_n == 0:
            _put(self.min_heap, number, lmin)
        elif min_n == max_n:
            if number > self.getMedian():
                _put(self.min_heap, number, lmin)
            else:
                _put(self.max_heap, number, lmax)
        elif min_n > max_n:
            if number > self.getMedian():
                _put(self.max_heap, self.min_heap[1], lmax)
                _pop(self.min_heap, lmax)
                _put(self.min_heap, number, lmin)
            else:
                _put(self.max_heap, number, lmax)
        else:
            if number > self.getMedian():
                _put(self.min_heap, number, lmin)
            else:
                _put(self.min_heap, self.max_heap[1], lmin)
                _pop(self.max_heap, lmin)
                _put(self.max_heap, number, lmax)


def main():
    ok = True

    a = MinMaxHeap()

    for i in range(1, 8):
        arr = []
        for _ in range(10 ** i):
            x = randint(0, 100000)
            a.put(x)
            arr.append(x)

        binmed = a.getMedian()
        a.clear()
        statmed = median(arr)

        print('Test:', i, "size:", 10 ** i, binmed, " = ", statmed, binmed == statmed)

    if ok: print("Passed")


if __name__ == "__main__": main()
