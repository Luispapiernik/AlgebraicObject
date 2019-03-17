MATRIX = 0
DICT = 1


class MAthError(Exception):
    pass


class OperationOutOfDomainError(MAthError):
    def __init__(self):
        self.args = ('operation out of domain',)


class ElementsWithoutOperationError(MAthError):
    def __init__(self):
        self.args = ('elements without operations',)


class SemiGroup(object):
    """Esta clase representa un semigrupo, un semigrupo es un conjunto no vacio
       S con una operacion binaria multiplicacion (*): S x S -> S

       Atributos
       ---------
       name: nombre del semigrupo
       elements: conjunto con los elementos del semigrupo
       multiplicacionTable: diccionario que especifica como realizar la
            operacion con los elementos del semigrupo
       """

    def __init__(self, name, elements, multiplicationTable, format=MATRIX):
        """name: nombe del semigrupo
           elements: iterable con los elementos del semigrupo
           multiplicationTable: dict o list, es la tabla de multiplicacion.
                Si se pasa un diccionario, la clave es una tupla de elementos
                y el valor es un elemento, es decir, dict[(a, b)] = c esto
                representa la operacion a * b = c. Si se pasa una matriz(lista
                de listas)la primera fila y la primera columna especifican
                como se operan los elementos, es decir, el valor de
                matriz[i][j] reprensenta a[i] * b[j] donde a[i] es la i-esima
                componente de la columan 1 y b[j] es la j-esima componente de
                la fila j
           format: MATRIX=0 o DICT=1, indica en que formato se ingreso la tabla
                de multiplicacion"""

        self.name = name

        if format == MATRIX:
            self._check_table(elements, multiplicationTable)

            self.elements = set(elements)
            self.multiplicationTable = multiplicationTable

    def _check_table(self, elements, table):
        """Esta funcion retorna True si table es una table de multiplicacion
           valida. Una tabla es validad si para todo par de elementos de
           elements esta definida la operacion, ademas no puede tener
           operaciones fuera del dominio

           parametros
           ----------
           elements: iterable con los elementos del semigrupo
           table: list. Tabla de multiplicacion a testear
           """
        # mirar que la operacion esta definida para todo par de elementos
        subset = set(table[0])  # elementos en la primera fila
        for element in elements:
            if not (element in subset):
                raise ElementsWithoutOperationError()

        # elementos en la primera columna
        subset = set([table[i][0] for i in range(len(table))])
        for element in elements:
            if not (element in subset):
                raise ElementsWithoutOperationError()

        # la tabla de multiplicacion esta dentro del dominio
        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                if not(table[i][j] in elements):
                    raise OperationOutOfDomainError()

        return True


def main():
    pass


if __name__ == '__main__':
    main()
