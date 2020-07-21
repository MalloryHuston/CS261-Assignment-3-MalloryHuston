# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 3, Part 1
# Description: Implementation of a singly linked list data structure.


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Places new node immediately after front sentinel
        """
        # be careful to first set new_node.next to 1st non-sentinel node, then point head to new_node
        new_node = SLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        Places new node immediately prior to back sentinel
        """
        # initialize new_node and set new_node.next to point to the back sentinel
        new_node = SLNode(value)
        new_node.next = self.tail

        # loop through LinkedList in search of node currently residing immediately prior to tail
        insert_after = self.head
        while insert_after.next != self.tail:
            insert_after = insert_after.next

        # point insert_after node toward our new_node
        insert_after.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts new SLNode object at specified index
        """
        # handle case where index < 0
        if index < 0:
            raise SLLException

        # initialize new_node and reference with a convenient variable
        new_node = SLNode(value)

        # iterate through LinkedList in search of node to insert new_node immediately after
        insert_after = self.head
        for i in range(index):
            if insert_after.next == self.tail:
                raise SLLException
            insert_after = insert_after.next

        # place new_node immediately after insert_after
        new_node.next = insert_after.next
        insert_after.next = new_node

    def remove_front(self) -> None:
        """
        Removes node immediately following LinkedList.head
        """
        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # remove first node via removing all references to it
        to_remove = self.head.next
        self.head.next = to_remove.next

    def remove_back(self) -> None:
        """
        Removes node immediately prior to LinkedList.tail
        """
        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # iterate through LinkedList in search of SLNode object to remove
        current = self.head.next
        prior = self.head
        while current.next != self.tail:
            current = current.next
            prior = prior.next

        # remove current from LinkedList by pointing prior to tail
        prior.next = current.next

    def remove_at_index(self, index: int) -> None:
        """
        Removes SLNode at specified index in LinkedList
        """
        # handle case where index < 0
        if index < 0:
            raise SLLException

        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # iterate through nodes in search of index to remove
        current = self.head.next
        prior = self.head
        i = 0
        while i != index:
            # handle case where index is out of range
            if current.next == self.tail:
                raise SLLException
            current = current.next
            prior = prior.next
            i += 1

        # now current is node at specified index, so remove current
        prior.next = current.next

    def get_front(self) -> object:
        """
        Returns first non-head node value without removal
        """
        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # return expected object/value
        return self.head.next.value

    def get_back(self) -> object:
        """
        Returns last non-tail node value without removal
        """
        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # iterate through LinkedList in search of last no-tail node
        last_node = self.head.next
        while last_node.next != self.tail:
            last_node = last_node.next

        # return expected object/value
        return last_node.value

    def remove(self, value: object) -> bool:
        """
        Removes first node containing value argument and indicates if successful
        """
        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            return False

        # iterate through nodes in search of matching value property
        current = self.head.next
        prior = self.head
        while current != self.tail and current.value != value:
            current = current.next
            prior = prior.next

        # handle case where value was not found in the LinkedList
        if current == self.tail:
            return False

        # handle case where value was found in the LinkedList
        prior.next = current.next
        return True

    def count(self, value: object) -> int:
        """
        Counts number of non-head/tail elements that have value property matching argument
        """
        # iterate through LinkedList while counting each 'hit' once
        count = 0
        current = self.head
        while current.next != self.tail:
            current = current.next
            if current.value == value:
                count += 1
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList based on arguments passed
        """
        # handle case where start_index < 0
        if start_index < 0:
            raise SLLException

        # handle case where LinkedList is empty
        if self.head.next == self.tail:
            raise SLLException

        # iterate through list in search of node located at start_index
        index = 0
        current = self.head.next
        while index != start_index and current.next != self.tail:
            current = current.next
            index += 1

        # handle case where index out of range
        if index != start_index:
            raise SLLException

        # build new LinkedList while checking whether offset falls out of range
        new_LL = LinkedList()
        for count in range(size):
            new_LL.add_back(current.value)
            # handle case where offset is out of range
            if current.next == self.tail and count < size - 1:
                raise SLLException
            current = current.next

        return new_LL

    def is_sorted(self) -> int:
        """
        Indicates whether LinkedList is sorted
        """
        # handle case where LinkedList is empty or contains a single node
        if self.length() < 2:
            return 1

        # iterate through list to determine whether it is strictly ascending/descending
        strictly_ascending = True
        strictly_descending = True
        current = self.head.next
        prior = self.head
        while current.next != self.tail:
            current = current.next
            prior = prior.next
            # handle case where pair of nodes is not strictly ascending
            if current.value <= prior.value:
                strictly_ascending = False
            # handle case where pair of nodes is not strictly descending
            if current.value >= prior.value:
                strictly_descending = False

        # return indicator to user based on findings in while-loop
        if strictly_ascending:
            return 1
        elif strictly_descending:
            return 2
        else:
            return 0

    def length(self) -> int:
        """
        Returns number of non-head/tail nodes in LinkedList
        """
        # iterate through LinkedList while counting each node once
        count = 0
        current = self.head
        while current.next != self.tail:
            current = current.next
            count += 1
        return count

    def is_empty(self) -> bool:
        """
        Indicates whether LinkedList is empty
        """
        if self.head.next == self.tail:
            return True
        else:
            return False


if __name__ == '__main__':

    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
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
    list = LinkedList(['A', 'B'])
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
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())

    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)

    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))

    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")

    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
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
        list = LinkedList(case)
        print('Result:', list.is_sorted(), list)

    print('\n# is_empty example 1')
    list = LinkedList()
    print(list.is_empty(), list)
    list.add_back(100)
    print(list.is_empty(), list)
    list.remove_at_index(0)
    print(list.is_empty(), list)

    print('\n# length example 1')
    list = LinkedList()
    print(list.length())
    for i in range(800):
        list.add_front(i)
    print(list.length())
    for i in range(799, 300, -1):
        list.remove_at_index(i)
    print(list.length())
