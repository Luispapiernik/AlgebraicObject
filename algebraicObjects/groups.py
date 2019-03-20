from algebraicObjects.monoids import Monoid
from algebraicObjects import MathError
from algebraicObjects import MATRIX


class ElementWithoutInverseError(MathError):
    def __init__(self):
        self.args = ('element without inverse',)


class Group(Monoid):
    """
        Esta clase representa un grupo finito, un grupo finito es un monoide
        en el que todos los elementos son invertibles.

        Atributos
        ---------
        name: nombre del semigrupo
        elements: conjunto con los elementos del semigrupo
        multiplicacionTable: diccionario que especifica como realizar la
            operacion con los elementos del semigrupo
        format: indica en que formato se ingresara la tabla de multiplicacion
    """

    def __init__(self, name, elements, multiplicationTable, format=MATRIX):
        super(Group, self).__init__(name, elements, multiplicationTable,
                                    format)

        # todos los elementos deben ser invertibles
        for element in elements:
            if not super(Group, self).has_inverse(element):
                raise ElementWithoutInverseError()


def main():
    pass


if __name__ == '__main__':
    main()
