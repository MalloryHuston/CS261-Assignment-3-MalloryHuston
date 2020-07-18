# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 3, Part 2
# Description: Implementation of a circular doubly linked list data structure.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        return

    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        return

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        return 0

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        return 0

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def slice(self, start_index: int, size: int) -> object:
        """
        TODO: Write this implementation
        """
        return CircularList()

    def is_sorted(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """
        return

    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        return

    def length(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True


if __name__ == '__main__':
    print('\n# add_front example 1')
    list = CircularList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)

    print('\n# add_back example 1')
    list = CircularList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)

    print('\n# insert_at_index example 1')
    list = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    list = CircularList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    list = CircularList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)

    print('\n# remove_at_index example 1')
    list = CircularList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)

    print('\n# get_front example 1')
    list = CircularList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    list = CircularList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())

    print('\n# remove example 1')
    list = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)

    print('\n# count example 1')
    list = CircularList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))

    print('\n# slice example 1')
    list = CircularList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")

    print('\n# slice example 2')
    list = CircularList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200]
    )
    for case in test_cases:
        list = CircularList(case)
        print('Result:', list.is_sorted(), list)

    print('\n# is_empty example 1')
    list = CircularList()
    print(list.is_empty(), list)
    list.add_back(100)
    print(list.is_empty(), list)
    list.remove_at_index(0)
    print(list.is_empty(), list)

    print('\n# length example 1')
    list = CircularList()
    print(list.length())
    for i in range(800):
        list.add_front(i)
    print(list.length())
    for i in range(799, 300, -1):
        list.remove_at_index(i)
    print(list.length())

    print('\n# swap_pairs example 1')
    list = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            list.swap_pairs(i, j)
            print(list)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        list = CircularList(case)
        list.reverse()
        print(list)

    print('\n# reverse example 2')
    list = CircularList()
    print(list)
    list.reverse()
    print(list)
    list.add_back(2)
    list.add_back(3)
    list.add_front(1)
    list.reverse()
    print(list)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        list = CircularList(case)
        print(list)
        list.sort()
        print(list)
