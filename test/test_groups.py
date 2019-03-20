from algebraicObjects.groups import Group
from algebraicObjects.groups import ElementWithoutInverseError
import unittest


class Test_Groups(unittest.TestCase):
    def test_initialization(self):
        group = Group('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                        [0, 0, 1, 2],
                                        [1, 1, 2, 0],
                                        [2, 2, 0, 1]])

        self.assertIsInstance(group, Group)

        group = Group('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                        [0, 0, 1, 2],
                                        [1, 1, 2, 0],
                                        [2, 2, 0, 1]])

        self.assertRaises(ElementWithoutInverseError, Group,
                          'Z3', [0, 1, 2], [[0, 0, 1, 2],
                                            [0, 0, 1, 2],
                                            [1, 1, 2, 1],
                                            [2, 2, 0, 1]])


def main():
    pass


if __name__ == '__main__':
    main()
