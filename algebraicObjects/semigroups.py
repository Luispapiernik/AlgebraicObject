MATRIX = 0
DICT = 1


class SemiGroup(object):
    """Esta clase representa un semigrupo, es un conjunto no vacio S con una
       operacion binaria (+): S x S -> S"""

    def __init__(self, name, elements, multiplicationTable, format=MATRIX):
        """name: nombe del semigrupo
           elements: iterable con los elementos del semigrupo
           multiplicationTable: dict o list, es la tabla de multiplicacion.
                Si se pasa un diccionario, la clave es una tupla de elementos
                y el valor es un elemento, es decir, dict[(a, b)] = c esto
                representa la operacion a + b = c. Si se pasa una matriz(lista
                de listas) la primera fila y la primera columna especifican
                como se operan los elementos, es decir, el valor de
                matriz[i][j] reprensenta a[i] * b[j] donde a[i] es la i-esima
                componente de la columan 1 y b[j] es la j-esima componente de
                la fila j
           format: MATRIX=0 o DICT=1, indica en que formato se ingreso la tabla
                de multiplicacion"""

        self.name = name
        self.format = format
        self.elements = set(elements)
        self.multiplicationTable = multiplicationTable


def main():
    pass


if __name__ == '__main__':
    main()
