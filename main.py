from random import randint
from typing import Any, Optional

from exceptions import FullListError, NoSuchElementError, NoSuchIndexError, NotSameTypeError
from time_decorator import timer_factory
import logging


class Node:
    value_type = None

    def __init__(self, value: Optional[Any] = None):
        self.value = value
        self.next_node = None

    def validate(self):
        if type(self.value) != self.value_type:
            raise NotSameTypeError(f'Value must be of type {self.value_type.__name__}')


class LinkedList:
    def __init__(self, size: Optional[int] = None):
        self.max_size = size
        self.head_node = None
        self._number_of_elements = 0
        self._type = None

        self.logging = False

    def get_node_class(self) -> type(Node):
        class LinkedListNode(Node):
            value_type = self._type
        return LinkedListNode

    def get_node(self, value: Any) -> Node:
        node_class = self.get_node_class()
        node = node_class(value)
        node.validate()
        return node

    def validate(self):
        if self.max_size is not None and self._number_of_elements >= self.max_size:
            raise FullListError()

    def add_node(self, node: Node):
        if self.head_node is None:
            self.head_node = node
        else:
            self.last_node.next_node = node
        self._number_of_elements += 1

    def push(self, value: Any):
        self.validate()
        if not self._type:
            self._type = type(value)
        new_node = self.get_node(value)
        self.add_node(new_node)

    @property
    def last_node(self) -> Optional[Node]:
        *_, last = self
        return last

    def __iter__(self):
        curr_node = self.head_node
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next_node

    def __len__(self):
        return self._number_of_elements

    def print(self):
        return ', '.join(str(node.value) for node in self)

    def delete_node(self, prev_node: Optional[Node], node: Node):
        value = node.value
        if prev_node is None:
            self.head_node = node.next_node
        else:
            prev_node.next_node = node.next_node
        self._number_of_elements -= 1
        return value

    @timer_factory('LinkedList pop by index')
    def pop_by_index(self, index: int) -> Any:
        prev_node = None
        for node_index, node in enumerate(self):
            if index == node_index:
                return self.delete_node(prev_node, node)
            prev_node = node
        raise NoSuchIndexError()

    def pop_by_value(self, value: Any) -> Any:
        prev_node = None
        for node in self:
            if node.value == value:
                return self.delete_node(prev_node, node)
            prev_node = node
        raise NoSuchElementError()

    @timer_factory('LinkedList pop by value')
    def pop_single_value(self, value: Any) -> Any:
        return self.pop_by_value(value)

    @timer_factory('LinkedList pop all by value')
    def pop_all_values(self, value: Any) -> Any:
        while True:
            try:
                self.pop_by_value(value)
            except NoSuchElementError:
                break

