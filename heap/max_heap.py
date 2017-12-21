from nose.tools import assert_equal


class MaxHeap(object):

    def __init__(self, data):
        """
        build max heap, O(n)
        :param data:
        """
        self.array = data
        self._build_max_heap()

    def _build_max_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self._max_heapify(index=i, array_length=len(self.array))

    def _max_heapify(self, index, array_length):
        """
        similar to bubble down. Correct a single violation of the heap property in a subtree
        find maximum children. If greater than current, move down current, otherwise stop
        or find the larges of three and compare with current
        :param index: index to start heapify (bubble down)
        :param stop_ind: index to stop heapify (the index of right most leaf node)
        :return:
        """
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        largest_index = index
        if left_child_index < array_length and self.array[index] < self.array[left_child_index]:
            largest_index = left_child_index
        if right_child_index < array_length and self.array[largest_index] < self.array[right_child_index]:
            largest_index = right_child_index
        if largest_index != index:
            self.array[index], self.array[largest_index] = self.array[largest_index], self.array[index]
            self._max_heapify(index=largest_index, array_length=array_length)

    def insert(self, key):
        if key is None:
            raise TypeError("illegal argument")
        self.array.append(key)
        self._bubble_up(len(self.array) - 1);

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.array[parent_index] < self.array[index]:
            self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
            self._bubble_up(parent_index)

    def extract_max(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)
        maximum = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop(-1)
        self._max_heapify(index=0, array_length=len(self.array))
        return maximum

    def peek_max(self):
        return self.array[0] if self.array else None

    def heap_sort(self):
        """
        minheap---> descending order
        maxheap---> ascending order
        :return:
        """
        unfinished_size = len(self.array)
        while unfinished_size != 0:
            self.array[0], self.array[unfinished_size - 1] = self.array[unfinished_size - 1], self.array[0]
            unfinished_size -= 1
            self._max_heapify(index=0, array_length=unfinished_size)


class TestMaxHeap(object):

    def test_max_heap(self):
        heap = MaxHeap([])
        assert_equal(heap.peek_max(), None)
        assert_equal(heap.extract_max(), None)
        heap.insert(20)
        assert_equal(heap.peek_max(), 20)
        heap.insert(5)
        assert_equal(heap.peek_max(), 20)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(5)
        assert_equal(heap.peek_max(), 40)
        heap.insert(41)
        assert_equal(heap.peek_max(), 41)
        assert_equal(heap.extract_max(), 41)
        assert_equal(heap.peek_max(), 40)
        print('Success: test_max_heap')
        print(heap.array)

    def test_max_heap2(self):
        heap = MaxHeap([11, 54, 3, 8, 6, 27, 18, 20])
        print(heap.array)
        heap.heap_sort()
        print(heap.array)


def main():
    test = TestMaxHeap()
    test.test_max_heap2()


if __name__ == '__main__':
    main()