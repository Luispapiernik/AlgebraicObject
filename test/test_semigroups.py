from algebraicObjects.semigroups import SemiGroup
from algebraicObjects.semigroups import OperationOutOfDomainError
from algebraicObjects.semigroups import ElementsWithoutOperationError
from algebraicObjects.semigroups import MultivaluedOperation
from algebraicObjects.semigroups import DICT
from algebraicObjects.semigroups import SemigroupWithoutUnit
from algebraicObjects.semigroups import ElementWithoutInverse


import unittest


class Test_SemiGroup(unittest.TestCase):
    def test_initializationWithMatrix(self):
        # tabla correcta
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertIsInstance(semigroup, SemiGroup)

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 2, 1],
                                                [0, 0, 2, 1],
                                                [2, 2, 1, 0],
                                                [1, 1, 0, 2]])

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
                                      (1, 0): 1, (1, 2): 0, (0, 4): 1,
                                      (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        # para diccionario es imposible que a un par de elementos se le asocien
        # dos o mas valores, entonces no se necesita testear ese caso

    # @unittest.skip('en construccion')
    def test_check_associativity(self):
        # tabla asociativa
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertTrue(semigroup._check_associativity())

        # tabla no asociativa '2' * '1' = '0' pero '1' * '2' = '2'
        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '1', '2'],
                                            ['1', '1', '2', '2'],
                                            ['2', '2', '0', '1']])

        self.assertFalse(semigroup._check_associativity())

        # tabla asociativa
        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertTrue(semigroup._check_associativity())

        # tabla no asociativa 2 * 1 = 0 pero 1 * 2 = 2
        semigroup = SemiGroup('Z3', [0, 1, 2],
                              {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                               (1, 0): 1, (1, 1): 2, (1, 2): 2,
                               (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        self.assertFalse(semigroup._check_associativity())

    def test_op(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.op(1, 2), 0)
        self.assertEqual(semigroup.op(2, 2), 1)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertEqual(semigroup.op('1', '1'), '2')
        self.assertEqual(semigroup.op('0', '2'), '2')

    def test_isin(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertTrue(semigroup.isin(1))
        self.assertFalse(semigroup.isin(4))

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertFalse(semigroup.isin('4'))
        self.assertFalse(semigroup.isin(4))
        self.assertTrue(semigroup.isin('0'))

    def test_has_unit(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.has_unit(), 0)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertEqual(semigroup.has_unit(), '0')

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 1],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertFalse(semigroup.has_unit())

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '2',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertFalse(semigroup.has_unit())

    def test_unit(self):
        # se llamara 2 veces al metodo unit para verificar que la cache
        # funciones bien
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.unit(), 0)
        self.assertEqual(semigroup.unit(), 0)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertEqual(semigroup.unit(), '0')
        self.assertEqual(semigroup.unit(), '0')

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 1],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertIsNone(semigroup.unit())
        self.assertIsNone(semigroup.unit())

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '2',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertIsNone(semigroup.unit())
        self.assertIsNone(semigroup.unit())

    def test_check_commutativity(self):
        # se llamara 2 veces al metodo check_commutativity para verificar que
        # la cache funciones bien
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertTrue(semigroup.check_commutativity())
        self.assertTrue(semigroup.check_commutativity())

        # semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
        #                                         [0, 0, 1, 0],
        #                                         [1, 2, 1, 0],
        #                                         [2, 2, 0, 1]])

        # self.assertFalse(semigroup.check_commutativity())
        # self.assertEqual(semigroup.check_commutativity(True),
        #                  {(0, 1): 1, (1, 0): 2})

        # tabla no conmutativa '2' * '1' = '0' pero '1' * '2' = '2'
        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '1', '2'],
                                            ['1', '1', '2', '2'],
                                            ['2', '2', '0', '1']])

        self.assertEqual(semigroup.check_commutativity(True),
                         {('1', '2'): '2', ('2', '1'): '0'})
        self.assertFalse(semigroup.check_commutativity())
        self.assertEqual(semigroup.check_commutativity(True),
                         {('1', '2'): '2', ('2', '1'): '0'})
        self.assertFalse(semigroup.check_commutativity())

        # tabla conmutativa
        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertTrue(semigroup.check_commutativity())
        self.assertTrue(semigroup.check_commutativity())

        # tabla no conmutativa 2 * 1 = 0 pero 1 * 2 = 2
        semigroup = SemiGroup('Z3', [0, 1, 2],
                              {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                               (1, 0): 1, (1, 1): 2, (1, 2): 2,
                               (2, 0): 2, (2, 1): 0, (2, 2): 1}, DICT)

        self.assertEqual(semigroup.check_commutativity(True),
                         {(2, 1): 0, (1, 2): 2})
        self.assertFalse(semigroup.check_commutativity())

    def test_has_right_inverse(self):
        # se llamara 2 veces al metodo has_right_inverse para verificar que
        # la cache funciones bien
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])
        for element in range(3):
            self.assertTrue(semigroup.has_right_inverse(element))
            self.assertTrue(semigroup.has_right_inverse(element))

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 2],
                                                [2, 2, 2, 1]])
        self.assertTrue(semigroup.has_right_inverse(0))
        self.assertFalse(semigroup.has_right_inverse(1))

        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '2', '2'],
                                            ['1', '1', '2', '2'],
                                            ['2', '2', '0', '1']])

        self.assertRaises(SemigroupWithoutUnit, semigroup.has_right_inverse, '1')

    def test_right_inverse(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.right_inverse(0), 0)
        self.assertEqual(semigroup.right_inverse(1), 2)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertEqual(semigroup.right_inverse('0'), '0')
        self.assertEqual(semigroup.right_inverse('1'), '2')

        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '1', '2'],
                                            ['1', '1', '2', '2'],
                                            ['2', '2', '0', '1']])

        self.assertRaises(ElementWithoutInverse, semigroup.right_inverse, '1')

    def test_has_left_inverse(self):
        # se llamara 2 veces al metodo has_left_inverse para verificar que
        # la cache funciones bien
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])
        for element in range(3):
            self.assertTrue(semigroup.has_left_inverse(element))
            self.assertTrue(semigroup.has_left_inverse(element))

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 2, 1]])
        self.assertTrue(semigroup.has_left_inverse(0))
        self.assertFalse(semigroup.has_left_inverse(1))

        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '2', '2'],
                                            ['1', '1', '2', '2'],
                                            ['2', '2', '0', '1']])

        self.assertRaises(SemigroupWithoutUnit, semigroup.has_left_inverse, '1')

    # @unittest.skip('En construccion')
    def test_left_inverse(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.left_inverse(0), 0)
        self.assertEqual(semigroup.left_inverse(1), 2)

        semigroup = SemiGroup('Z3', '012',
                              {('0', '0'): '0', ('0', '1'): '1',
                               ('0', '2'): '2', ('1', '0'): '1',
                               ('1', '1'): '2', ('1', '2'): '0',
                               ('2', '0'): '2', ('2', '1'): '0',
                               ('2', '2'): '1'}, DICT)

        self.assertEqual(semigroup.left_inverse('0'), '0')
        self.assertEqual(semigroup.left_inverse('1'), '2')

        semigroup = SemiGroup('Z3', '012', [['0', '0', '1', '2'],
                                            ['0', '0', '1', '2'],
                                            ['1', '1', '2', '0'],
                                            ['2', '2', '2', '1']])

        self.assertRaises(ElementWithoutInverse, semigroup.left_inverse, '1')

    def test_inverse(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        for element in range(3):
            self.assertTrue(semigroup.has_inverse(element))

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 2, 1]])

        self.assertFalse(semigroup.has_inverse(1))

    @unittest.skip('En construccion')
    def test_commutators(self):
        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 2],
                                                [1, 1, 2, 0],
                                                [2, 2, 0, 1]])

        for element in [0, 1, 2]:
            self.assertEqual(semigroup.commutators(element), set([0, 1, 2]))

        semigroup = SemiGroup('Z3', [0, 1, 2], [[0, 0, 1, 2],
                                                [0, 0, 1, 0],
                                                [1, 2, 1, 0],
                                                [2, 2, 0, 1]])

        self.assertEqual(semigroup.commutators(1), set([1, 2]))


def main():
    pass


if __name__ == '__main__':
    main()
