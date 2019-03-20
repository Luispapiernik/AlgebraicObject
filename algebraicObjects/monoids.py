from algebraicObjects.semigroups import SemiGroup
from algebraicObjects import MathError
from algebraicObjects import MATRIX


class IsNotMonoidError(MathError):
    def __init__(self):
        self.args = ('The set does not have a monoid strucure, there is not unit',)


class Monoid(SemiGroup):
    """
        Esta clase representa un monoide finito, un monoide es un semigrupo con
        unidad

        Atributos
        ---------
        name: nombre del semigrupo
        elements: conjunto con los elementos del semigrupo
        multiplicacionTable: diccionario que especifica como realizar la
            operacion con los elementos del semigrupo
        format: indica en que formato se ingresara la tabla de multiplicacion
    """
    def __init__(self, name, elements, multiplicationTable, format=MATRIX):
        super(Monoid, self).__init__(name, elements, multiplicationTable,
                                     format)

        # se debe testear que el semigrupo tenga un elemento identidad
        if not super(Monoid, self).has_unit():
            raise IsNotMonoidError()


def main():
    pass


if __name__ == '__main__':
    main()
