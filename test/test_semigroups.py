from algebraicObjects.semigroups import SemiGroup, MATRIX, DICT

import unittest


class Test_SemiGroup(unittest.TestCase):
    def test_canInstanceSemiGroupMatrixFormat(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 3],
                                                [2, 2, 3, 4]])

        self.assertEqual(semigroup.format, MATRIX)
        self.assertIsInstance(semigroup, SemiGroup)

    def test_canInstanceSemiGroupDictFormat(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], {(i, j): (
            i + j) % 3 for i in range(3) for j in range(3)}, DICT)

        self.assertEqual(semigroup.format, DICT)
        self.assertIsInstance(semigroup, SemiGroup)


def main():
    pass


if __name__ == '__main__':
    main()
