import unittest

from main import LinkedList
from exceptions import FullListError, NoSuchElementError, NoSuchIndexError, NotSameTypeError


class TestOneWayArray(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_push(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(self.linked_list.last_node.value, 2)

    def test_max_size(self):
        self.linked_list.size = 1
        self.linked_list.push(1)
        with self.assertRaises(FullListError):
            self.linked_list.push(2)

    def test_same_type(self):
        self.linked_list.push(1)
        with self.assertRaises(NotSameTypeError):
            self.linked_list.push('a')

    def test_pop_by_index(self):
        self.linked_list.push('a')
        self.linked_list.push('b')

        self.linked_list.pop_by_index(index=0)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list.head_node.value, 'b')

    def test_pop_by_value(self):
        self.linked_list.push('a')
        self.linked_list.push('b')

        self.linked_list.pop_single_value('a')
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list.head_node.value, 'b')

    def test_pop_multiple_by_value(self):
        self.linked_list.push('a')
        self.linked_list.push('a')
        self.linked_list.push('b')

        self.linked_list.pop_all_values('a')
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list.head_node.value, 'b')

    def test_pop_no_index_value(self):
        with self.assertRaises(NoSuchIndexError):
            self.linked_list.pop_by_index(0)

    def test_pop_no_value(self):
        with self.assertRaises(NoSuchElementError):
            self.linked_list.pop_single_value('a')


if __name__ == '__main__':
    unittest.main()