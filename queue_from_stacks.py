# Course: CS261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 3, Part 4
# Description: Implementation of the Two-Stack Queue ADT class
#              as well as using the MaxStack ADT as underlying
#              code for the Queue ADT.

from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds new node immediately after the head of the LinkedList
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue
        """
        # handle case where queue is empty
        if self.s1.is_empty():
            raise QueueException

        # iterate through Queue.s1 and enqueue items into MaxStack.s2
        value = None
        while not self.s1.is_empty():
            value = self.s1.pop()
            self.s2.push(value)

        # pop top item off of Queue.s2 because it should be removed from Queue
        self.s2.pop()

        # enqueue elements from Queue.s2 back into Queue.s1
        while not self.s2.is_empty():
            temp = self.s2.pop()
            self.s1.push(temp)

        # return value from the beginning of the Queue
        return value

    def is_empty(self) -> bool:
        """
        Indicates whether the Queue is empty (no elements)
        """
        if self.s1.is_empty():
            return True
        else:
            return False

    def size(self) -> int:
        """
        Returns the number of elements in the Queue
        """
        return self.s1.size()


# BASIC TESTING
if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n# is_empty example 1')
    q = Queue()
    print(q.is_empty())
    q.enqueue(10)
    print(q.is_empty())
    q.dequeue()
    print(q.is_empty())

    print('\n# size example 1')
    q = Queue()
    print(q.size())
    for value in [1, 2, 3, 4, 5, 6]:
        q.enqueue(value)
    print(q.size())
