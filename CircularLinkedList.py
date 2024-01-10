import random

class CircularLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def roll_dice(self):
        n = 0
        rand = random.Random()
        n = rand.randint(1, 6)
        if n == 6:
            n += rand.randint(1, 6)
        if n == 12:
            n += rand.randint(1, 6)
        if n == 18:
            return 0
        return n

    def first(self):
        if self.is_empty():
            return None
        return self.tail.next.data

    def get_last(self):
        if self.is_empty():
            return None
        return self.tail.data

    def rotate(self):
        if not self.is_empty():
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, data):
        if self.size == 0:
            self.tail = self.Node(data)
            self.tail.next = self.tail
            self.size += 1
        else:
            node = self.Node(data)
            node.next = self.tail.next
            self.tail.next = node
            self.size += 1

    def add_last(self, data):
        self.add_first(data)
        self.tail = self.tail.next
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        return head.data

    def remove_last(self):
        if self.is_empty():
            return None
        head = self.tail
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        return head.data

    def print_linked_list(self):
        current = self.tail.next
        if self.tail is not None:
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.tail.next:
                    break
            print()

    def split_print(self):
        current = self.tail.next
        T = self.size // 2
        i = 1

        while True:
            print(current.data, end=" ")
            current = current.next
            i += 1
            if current == self.tail.next or i > T:
                break
        print()

        while True:
            print(current.data, end=" ")
            current = current.next
            T += 1
            if current == self.tail.next or T > self.size:
                break
        print()
