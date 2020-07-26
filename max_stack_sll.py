# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 3, Part 2
# Description: Implementation of a stack built off of a singly linked list
#              structure. Implementation should also keep track of max value
#              of stack for O(1) getter method.

from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def push(self, value: object) -> None:
        """
        Adds node containing value to top of the stack
        """
        # add node to front of MaxStack.sll_val
        self.sll_val.add_front(value)

        # handle case where MaxStack.sll_max is empty
        if self.sll_max.is_empty():
            self.sll_max.add_front(value)

        # handle case where MaxStack.sll_max is not empty
        current_max = self.sll_max.get_front()
        if value > current_max:
            self.sll_max.add_front(value)
        else:
            self.sll_max.add_front(current_max)

    def pop(self) -> object:
        """
        Removes top element from stack and returns its value
        """
        # handle case where MaxStack is empty
        if self.sll_val.is_empty():
            raise StackException

        # maintain MaxStack.sll_max by removing front node
        self.sll_max.remove_front()

        # remove top element from MaxStack.sll_val and return value to user
        top_value = self.sll_val.get_front()
        self.sll_val.remove_front()
        return top_value

    def top(self) -> object:
        """
        Returns value of the top of the stack in a non-destructive manner
        """
        # handle case where stack is empty
        if self.sll_val.is_empty():
            raise StackException

        # get and return value from top of stack
        return self.sll_val.get_front()

    def is_empty(self) -> bool:
        """
        Indicates whether MaxStack is empty
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Returns the number of elements in the MaxStack
        """
        return self.sll_val.length()

    def get_max(self) -> object:
        """
        Returns maximum value currently stored in MaxStack
        """
        # handle case where MaxStack is empty
        if self.is_empty():
            raise StackException

        # return top value from the self.sll_max LinkedList
        return self.sll_max.get_front()


# BASIC TESTING
if __name__ == "__main__":
    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print('\n# pop example 1')
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print('\n# top example 1')
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)

    print('\n# is_empty example 1')
    s = MaxStack()
    print(s.is_empty())
    s.push(10)
    print(s.is_empty())
    s.pop()
    print(s.is_empty())

    print('\n# size example 1')
    s = MaxStack()
    print(s.size())
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s.size())

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
