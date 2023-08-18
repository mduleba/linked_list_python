from random import randint
import sys
from main import LinkedList
from time_decorator import timer_factory


@timer_factory('NormalList pop by index')
def array_pop_by_index(array, index):
    array.pop(index)


@timer_factory('NormalList pop by value')
def array_pop_by_value(array, value):
    for index, val in enumerate(array):
        if val == value:
            array.pop(index)
            break


@timer_factory('NormalList pop all by value')
def array_pop_all_values(array, value):
    for index, val in enumerate(array):
        if val == value:
            array.pop(index)


if __name__ == '__main__':
    linked_list = LinkedList(1000)
    normal_list = []
    for i in range(950):
        random_number = randint(0, 100)
        linked_list.push(random_number)
        normal_list.append(random_number)

    selected_number = 49
    for i in range(50):
        linked_list.push(selected_number)
        normal_list.append(selected_number)

    print(f'For Normal List length: {len(normal_list)}')
    print(f'For Linked List length: {len(linked_list)}')
    linked_list.pop_by_index(index=999)
    array_pop_by_index(normal_list, 999)

    linked_list.pop_single_value(selected_number)
    array_pop_by_value(normal_list, selected_number)

    linked_list.pop_all_values(selected_number)
    array_pop_all_values(normal_list, selected_number)



