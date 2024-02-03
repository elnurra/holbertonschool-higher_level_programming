#!/usr/bin/python3
"""Module that defines a singly linked list and its node."""


class Node:
    """Node class for a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute."""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class."""
    def __init__(self):
        """Initialize an empty Singly Linked List."""
        self.head = None

    def __str__(self):
        """Return a string representation of the linked list."""
        ret = ""
        node = self.head
        while node:
            ret += str(node.data) + "\n"
            node = node.next_node
        return ret[:-1]

    def sorted_insert(self, value):
        """Insert a new node with the given value in sorted order."""
        new = Node(value)
        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new.next_node = node.next_node
        node.next_node = new
