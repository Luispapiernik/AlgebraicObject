from algebraicObjects.semigroups import SemiGroup
from algebraicObjects.semigroups import OperationOutOfDomainError
from algebraicObjects.semigroups import ElementsWithoutOperationError

import unittest


class Test_SemiGroup(unittest.TestCase):
    def test_check_table(self):
        # tabla correcta
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertTrue(semigroup._check_table(semigroup.elements,
                                               semigroup.multiplicationTable))

        # tabla con operaciones fuera del conjunto de elementos
        self.assertRaises(OperationOutOfDomainError, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2],
                                      [0, 0, 1, 2],
                                      [1, 1, 2, 0],
                                      [2, 2, 0, 4]])

        # tabla sin especificacion de operacion para pares de elementos
        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 0],
                                      [0, 0, 1, 0],
                                      [1, 1, 2, 1],
                                      [2, 2, 0, 2]])


def main():
    pass


if __name__ == '__main__':
    main()
