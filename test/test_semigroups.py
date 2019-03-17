from algebraicObjects.semigroups import SemiGroup
from algebraicObjects.semigroups import OperationOutOfDomainError
from algebraicObjects.semigroups import ElementsWithoutOperationError
from algebraicObjects.semigroups import MultivaluedOperation
from algebraicObjects.semigroups import DICT


import unittest


class Test_SemiGroup(unittest.TestCase):
    def test_initializationWithMatrix(self):
        # tabla correcta
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertIsInstance(semigroup, SemiGroup)

        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '1', '2'],
                                            ['1', '1', '2', '0'],
                                            ['2', '2', '0', '1']])

        self.assertIsInstance(semigroup, SemiGroup)

        # tabla con operaciones fuera del conjunto de elementos
        self.assertRaises(OperationOutOfDomainError, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2],
                                      [0, 0, 1, 2],
                                      [1, 1, 2, 0],
                                      [2, 2, 0, 4]])

        # tabla sin especificacion de operacion para pares de elementos
        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1],
                                      [0, 0, 1],
                                      [1, 1, 2],
                                      [2, 2, 0]])

        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2],
                                      [0, 0, 1, 0],
                                      [2, 2, 0, 2]])

        # tablas con operacion multivaluada para pares de elementos
        self.assertRaises(MultivaluedOperation, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2, 2],
                                      [0, 0, 1, 2, 1],
                                      [1, 1, 2, 0, 2],
                                      [2, 2, 0, 1, 0]])

        self.assertRaises(MultivaluedOperation, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2],
                                      [0, 0, 1, 2],
                                      [1, 1, 2, 0],
                                      [2, 2, 0, 1],
                                      [1, 0, 1, 2]])

        self.assertRaises(MultivaluedOperation, SemiGroup, 'Z3',
                          [0, 1, 2], [[0, 0, 1, 2, 2],
                                      [0, 0, 1, 2, 1],
                                      [1, 1, 2, 0, 2],
                                      [2, 2, 0, 1, 0],
                                      [1, 0, 1, 2, 2]])

    def test_table2map(self):
        tableMatrix = [[0, 0, 1, 2],
                       [0, 0, 1, 2],
                       [1, 1, 2, 0],
                       [2, 2, 0, 1]]

        tableDict = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2,
                     (1, 2): 0, (2, 0): 2, (2, 1): 0, (2, 2): 1}

        semigroup = SemiGroup('Z3', [0, 1, 2], tableMatrix)

        self.assertEqual(semigroup._table2map(tableMatrix), tableDict)

    # @unittest.skip('test en construccion')
    def test_initializationWithDict(self):
        # tabla correcta
        semigroup = SemiGroup('Z3', [0, 1, 2],
                              {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                               (1, 0): 1, (1, 1): 2, (1, 2): 0,
                               (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        self.assertIsInstance(semigroup, SemiGroup)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertIsInstance(semigroup, SemiGroup)

        # tabla con operaciones fuera del conjunto de elementos
        self.assertRaises(OperationOutOfDomainError, SemiGroup, 'Z3',
                          [0, 1, 2], {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                                      (1, 0): 1, (1, 1): 2, (1, 2): 0,
                                      (2, 0): 2, (2, 1): 0, (2, 2): 4}, DICT)

        # tabla sin especificacion de operacion para pares de elementos
        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], {(0, 0): 0, (0, 1): 1,
                                      (1, 0): 1, (1, 1): 2,
                                      (2, 0): 2, (2, 1): 0}, DICT)

        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                                      (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        self.assertRaises(ElementsWithoutOperationError, SemiGroup, 'Z3',
                          [0, 1, 2], {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                                      (1, 0): 1, (1, 2): 0,
                                      (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        # tablas con operacion multivaluada para pares de elementos
        # self.assertRaises(MultivaluedOperation, SemiGroup, 'Z3',
        #                   [0, 1, 2], {(0, 0): 0, (0, 1): 1, (0, 2): 2,
        #                               (1, 0): 1, (1, 1): 2, (1, 2): 0,
        #                               (2, 0): 2, (2, 1): 0, (2, 2): 1,
        #                               (0, 2): 1}, DICT)


def main():
    pass


if __name__ == '__main__':
    main()
