import os
from decorator_2 import logger

path = 'file.log'

if os.path.exists(path):
    os.remove(path)

class FlatIterator:

    @logger(path)
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    @logger(path)
    def __iter__(self):
        self.cursor_list = 0
        self.cursor_item = 0
        return self

    @logger(path)
    def __next__(self):

        if self.cursor_list == len(self.list_of_list):
            raise StopIteration

        if self.cursor_item < len(self.list_of_list[self.cursor_list]) - 1:
            item = self.list_of_list[self.cursor_list][self.cursor_item]
            self.cursor_item += 1
        else:
            item = self.list_of_list[self.cursor_list][self.cursor_item]
            self.cursor_list += 1
            self.cursor_item = 0

        return item


@logger(path)
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
