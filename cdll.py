# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 3, Part 3
# Description: Implementation of a circular doubly linked list.


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
        Adds new node immediately after the sentinel
        """
        # initialize new node and set prev/next properties
        new_node = DLNode(value)
        new_node.prev = self.sentinel
        new_node.next = self.sentinel.next

        # link existing nodes of CircularList to new_node
        self.sentinel.next = new_node
        new_node.next.prev = new_node

    def add_back(self, value: object) -> None:
        """
        Adds new node immediately prior to the sentinel
        """
        # initialize new node and set prev/next properties
        new_node = DLNode(value)
        new_node.prev = self.sentinel.prev
        new_node.next = self.sentinel

        # link existing nodes of CircularList to new_node
        self.sentinel.prev = new_node
        new_node.prev.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts new node at specified index in CircularList
        """
        # handle case where index < 0
        if index < 0:
            raise CDLLException

        # iterate through list in search of node to insert new node after
        current = self.sentinel
        count = 0
        while count != index:
            current = current.next
            count += 1
            if current == self.sentinel:
                raise CDLLException

        # initialize new node and set next/prev properties
        new_node = DLNode(value)
        new_node.next = current.next
        new_node.prev = current

        # connect existing list to new_node
        current.next = new_node
        new_node.next.prev = new_node

    def remove_front(self) -> None:
        """
        Removes node immediately following the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        # remove node immediately following sentinel
        self.sentinel.next.next.prev = self.sentinel
        self.sentinel.next = self.sentinel.next.next

    def remove_back(self) -> None:
        """
        Removes node immediately prior to the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        # remove node immediately prior to sentinel
        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        Removes node at indicated index
        """
        # handle case where index < 0
        if index < 0:
            raise CDLLException

        # iterate through list in search of node to remove
        current = self.sentinel
        count = 0
        while count != index:
            current = current.next
            count += 1
            if current.next == self.sentinel:
                raise CDLLException

        # remove node following current
        current.next.next.prev = current
        current.next = current.next.next

    def get_front(self) -> object:
        """
        Returns value of node immediately following the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        # return value property from desired node
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Returns value of node immediately prior to the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        # return value property from desired node
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Removes first node with matching value property
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            return False

        # iterate through list in search of node to remove
        node_to_remove = self.sentinel.next
        index = 0
        while node_to_remove.value != value and node_to_remove != self.sentinel:
            node_to_remove = node_to_remove.next
            index += 1

        # handle case where value was not found in node properties
        if node_to_remove == self.sentinel:
            return False

        # handle case where value was found node_to_remove needs removed
        self.remove_at_index(index)
        return True

    def count(self, value: object) -> int:
        """
        Counts number of nodes with value property matching value argument
        """
        # iterate through nodes counting each matching value once
        count = 0
        current = self.sentinel
        while current.next != self.sentinel:
            current = current.next
            if current.value == value:
                count += 1
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new CircularList that is a subset of the current CircularList
        """
        # handle case where start_index is invalid
        if start_index < 0 or start_index > self.length() - 1:
            raise CDLLException

        # handle case where start_index + size offset is invalid
        if start_index + size - 1 > self.length() - 1:
            raise CDLLException

        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        # iterate through CircularList in search of starting node
        current = self.sentinel.next
        index = 0
        while index != start_index:
            current = current.next
            index += 1

        # iterate through nodes while adding them to the new CircularList
        new_CL = CircularList()
        for count in range(size):
            new_CL.add_back(current.value)
            current = current.next
        return new_CL

    def is_sorted(self) -> int:
        """
        Indicates whether CircularList node´s value properties are strictly
        ascending or descending
        """
        # handle case where CircularList has < 2 non-sentinel nodes
        if self.length() < 2:
            return 1

        # iterate through nodes while comparing adjacent nodes
        strictly_ascending = True
        strictly_descending = True
        current = self.sentinel.next.next
        prior = self.sentinel.next
        while current != self.sentinel:
            # handle case where prior and current are not strictly ascending
            if current.value <= prior.value:
                strictly_ascending = False

            # handle case where prior and current are not strictly descending
            if current.value >= prior.value:
                strictly_descending = False

            # iterate to next set of adjacent nodes
            current = current.next
            prior = prior.next

        # return indicator to user based on findings in while-loop
        if strictly_ascending:
            return 1
        elif strictly_descending:
            return 2
        else:
            return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes located at different indices
        """
        # handle case where CircularList is empty
        if self.is_empty():
            raise CDLLException

        # handle case where index1 is out of range
        if index1 < 0 or index1 > self.length() - 1:
            raise CDLLException

        # handle case where index2 is out of range
        if index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        # handle case where index1 == index2
        if index1 == index2:
            return

        # iterate through list in search of nodes to swap
        node_1 = self.sentinel.next
        node_1_index = 0
        node_2 = self.sentinel.next
        node_2_index = 0
        node_1_found = False
        node_2_found = False
        while not (node_1_found and node_2_found):
            # search for node_1
            if not node_1_found and node_1_index != index1:
                node_1 = node_1.next
                node_1_index += 1
            if not node_1_found and node_1_index == index1:
                node_1_found = True
            # search for node_2
            if not node_2_found and node_2_index != index2:
                node_2 = node_2.next
                node_2_index += 1
            if not node_2_found and node_2_index == index2:
                node_2_found = True

        # handle case where node_1.next == node_2
        if node_1.next == node_2:
            # link node_1 and node_2 to remainder of CircularList
            node_1.next = node_2.next
            node_2.prev = node_1.prev
            # link between node_1 and node_2
            node_2.next = node_1
            node_1.prev = node_2
            # link remainder of CircularList to node_1 and node_2
            node_2.prev.next = node_2
            node_1.next.prev = node_1

        # handle case where node_2.next == node_1
        elif node_2.next == node_1:
            # link node_1 and node_2 to remainder of CircularList
            node_2.next = node_1.next
            node_1.prev = node_2.prev
            # link between node_1 and node_2
            node_1.next = node_2
            node_2.prev = node_1
            # link remainder of CircularList to node_1 and node_2
            node_1.prev.next = node_1
            node_2.next.prev = node_2

        # handle case where node_1 and node_2 are not adjacent
        else:
            # remove node_1 from CircularList and point both pointers to its previous
            node_1.prev.next = node_1.next
            node_1.next.prev = node_1.prev
            node_1.next = node_1.prev

            # remove node_2 from CircularList and point both pointers to its previous
            node_2.prev.next = node_2.next
            node_2.next.prev = node_2.prev
            node_2.next = node_2.prev

            # swap prev pointers for both nodes
            node_1.prev = node_2.prev
            node_2.prev = node_1.next

            # swap next pointers for both nodes
            node_1.next = node_1.prev
            node_2.next = node_2.prev

            # re-insert node_1 into the list where node_2 used to live
            node_1.next = node_1.next.next
            node_1.next.prev = node_1
            node_1.prev.next = node_1

            # re-insert node_2 into the list where node_1 used to live
            node_2.next = node_2.next.next
            node_2.next.prev = node_2
            node_2.prev.next = node_2

    def reverse(self) -> None:
        """
        Reverses the order of the nodes in a CircularList
        """
        # create convenient variables to reference nodes to swap and their indices
        node_1 = self.sentinel.next
        node_2 = self.sentinel.prev
        index_1 = 0
        index_2 = self.length() - 1

        # iterate through Circular list swapping nodes until nodes converge
        while index_1 < index_2:
            # reference next nodes to swap prior to exchanging pointers
            new_node_1 = node_1.next
            new_node_2 = node_2.prev

            # handle case where node_1.next == node_2
            if node_1.next == node_2:
                # link node_1 and node_2 to remainder of CircularList
                node_1.next = node_2.next
                node_2.prev = node_1.prev
                # link between node_1 and node_2
                node_2.next = node_1
                node_1.prev = node_2
                # link remainder of CircularList to node_1 and node_2
                node_2.prev.next = node_2
                node_1.next.prev = node_1

            # handle case where node_2.next == node_1
            elif node_2.next == node_1:
                # link node_1 and node_2 to remainder of CircularList
                node_2.next = node_1.next
                node_1.prev = node_2.prev
                # link between node_1 and node_2
                node_1.next = node_2
                node_2.prev = node_1
                # link remainder of CircularList to node_1 and node_2
                node_1.prev.next = node_1
                node_2.next.prev = node_2

            # handle case where node_1 and node_2 are not adjacent
            else:
                # remove node_1 from CircularList and point both pointers to its previous
                node_1.prev.next = node_1.next
                node_1.next.prev = node_1.prev
                node_1.next = node_1.prev

                # remove node_2 from CircularList and point both pointers to its previous
                node_2.prev.next = node_2.next
                node_2.next.prev = node_2.prev
                node_2.next = node_2.prev

                # swap prev pointers for both nodes
                node_1.prev = node_2.prev
                node_2.prev = node_1.next

                # swap next pointers for both nodes
                node_1.next = node_1.prev
                node_2.next = node_2.prev

                # re-insert node_1 into the list where node_2 used to live
                node_1.next = node_1.next.next
                node_1.next.prev = node_1
                node_1.prev.next = node_1

                # re-insert node_2 into the list where node_1 used to live
                node_2.next = node_2.next.next
                node_2.next.prev = node_2
                node_2.prev.next = node_2

            # iterate to next set of nodes to swap and update indices
            node_1 = new_node_1
            node_2 = new_node_2
            index_1 += 1
            index_2 -= 1

    def sort(self) -> None:
        """
        Sorts the CircularList in non-descending order
        """
        # handle case where list contains less than 2 nodes
        if self.length() < 2:
            return

        # utilize bubble sort in sorting the CircularList
        outer_loop = self.length() - 1
        while outer_loop > 0:
            inner_loop = 0
            current = self.sentinel.next
            following = current.next
            while inner_loop < outer_loop:
                # handle case where next.value < current.value
                if following.value < current.value:
                    # swap nodes
                    current.next = following.next
                    following.prev = current.prev
                    following.next = current
                    current.prev = following
                    current.next.prev = current
                    following.prev.next = following
                    # update variables for next iteration
                    following = current.next
                    inner_loop += 1
                # handle case where next.value >= current.value
                else:
                    current = following
                    following = current.next
                    inner_loop += 1

            # update outer_loop variable for next iteration
            outer_loop -= 1

    def length(self) -> int:
        """
        Returns number of nodes in CircularList
        """
        # iterate through list while counting each node once
        count = 0
        current = self.sentinel
        while current.next != self.sentinel:
            current = current.next
            count += 1
        return count

    def is_empty(self) -> bool:
        """
        Indicates whether CircularList has zero non-sentinel nodes
        """
        return self.sentinel.next == self.sentinel


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
