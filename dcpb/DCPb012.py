# Problem 1.2: given an arr of int that are out of order,
# determine the bounds of the smallest window that must
# be sorted in order for the entire arr to be sorted.

import unittest


def dcpb012(array):
    left = get_left(array)
    if left == len(array):
        return 0, 0
    return left, get_right(array, left)


def get_left(array):
    left = i = 0
    while i < len(array):
        if array[i] < array[left]:
            return left
        left = i
        i += 1
    return i


def get_right(array, left):
    right = len(array) - 1
    i = 0
    while i < len(array):
        if (array[len(array) - 1 - i] > array[right]) or\
                (array[left] > array[right]):
            return right
        i += 1
        right = len(array) - i
    return False


class Test(unittest.TestCase):
    def test_array_correct(self):
        self.assertEqual(dcpb012([1, 2, 3, 4, 5]), (0, 0), "should be (0, 0)")

    def test_array_reverse(self):
        self.assertEqual(dcpb012([9, 8, 7, 6, 5, 4, 3, 2, 1]), (0, 8), "should be (0, 8)")

    def test_array_of_1(self):
        self.assertEqual(dcpb012([7]), (0, 0), "should be (0, 0)")

    def test_array_of_2(self):
        self.assertEqual(dcpb012([7, 3]), (0, 1), "should be (0, 1)")

    def test_array_of_5(self):
        self.assertEqual(dcpb012([3, 7, 5, 6, 9]), (1, 3), "should be (1, 3)")

    def test_array_of_8(self):
        self.assertEqual(dcpb012([1, 2, 3, 7, 5, 6, 4, 8]), (3, 6), "should be (3, 6)")

    def test_array_of_9(self):
        self.assertEqual(dcpb012([1, 3, 2, 7, 5, 6, 4, 8, 9]), (1, 6), "should be (1, 6)")


if __name__ == '__main__':
    unittest.main()
