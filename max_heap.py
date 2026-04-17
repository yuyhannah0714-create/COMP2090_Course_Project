class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        parent = self._parent(index)
        while index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    def _sift_down(self, index):
        size = len(self.heap)
        largest = index

        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def push(self, accid, balance):
        self.heap.append((balance, accid))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        if self.heap:
            self._sift_down(0)

        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def update_balance(self, accid, new_balance):
        for i, (balance, acc_id) in enumerate(self.heap):
            if acc_id == accid:
                self.heap[i] = (new_balance, accid)
                self._sift_up(i)
                self._sift_down(i)
                return True
        return False

    def is_empty(self):
        return len(self.heap) == 0

    def get_top_n(self, n):
        temp_heap = MaxHeap()
        temp_heap.heap = self.heap.copy()

        result = []
        for _ in range(min(n, len(self.heap))):
            if not temp_heap.is_empty():
                result.append(temp_heap.pop())

        return result

    def __len__(self):
        return len(self.heap)
