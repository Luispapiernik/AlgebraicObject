from algebraicObjects.monoids import Monoid
from algebraicObjects.monoids import IsNotMonoidError

import unittest


class Test_Monoids(unittest.TestCase):
    def test_initialization(self):
        # tabla correcta
        monoid = Monoid('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                          [0, 0, 1, 2],
                                          [1, 1, 2, 0],
                                          [2, 2, 0, 1]])

        self.assertIsInstance(monoid, Monoid)

        # tabla sin unidad
        self.assertRaises(IsNotMonoidError, Monoid, 'Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                                      [0, 1, 1, 2],
                                                                      [1, 1, 2, 0],
                                                                      [2, 2, 0, 1]])


def main():
    pass


if __name__ == '__main__':
    main()
