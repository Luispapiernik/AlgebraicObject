from random import choice


# constantes
MATRIX = 0
DICT = 1
RIGHT = 2
LEFT = 3


class MathError(Exception):
    pass


class OperationOutOfDomainError(MathError):
    def __init__(self):
        self.args = ('operation out of domain',)


class ElementsWithoutOperationError(MathError):
    def __init__(self):
        self.args = ('elements without operations',)


class MultivaluedOperation(MathError):
    def __init__(self):
        self.args = ('multivalued operation',)


class SemigroupWithoutUnit(MathError):
    def __init__(self, arg):
        self.args = (arg,)


class ElementWithoutInverse(MathError):
    """docstring for ElementWithoutInverse"""
    def __init__(self, type=RIGHT):
        if type == RIGHT:
            arg = 'element without right inverse'
        if type == LEFT:
            arg = 'element without left inverse'

        self.args = (arg,)


class SemiGroup(object):
    """
       Esta clase representa un semigrupo, un semigrupo es un conjunto no vacio
       S con una operacion binaria multiplicacion (*): S x S -> S

       Atributos
       ---------
       name: nombre del semigrupo
       elements: conjunto con los elementos del semigrupo
       multiplicacionTable: diccionario que especifica como realizar la
            operacion con los elementos del semigrupo
    """

    def __init__(self, name, elements, multiplicationTable, format=MATRIX):
        """
           name: nombe del semigrupo
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
                de multiplicacion
        """
        elements = set(elements)
        self.name = name

        if format == MATRIX:
            self._check_table(elements, multiplicationTable)

            self.elements = elements
            # self.multiplicationTable = multiplicationTable
            self.multiplicationTable = self._table2map(multiplicationTable)

        if format == DICT:
            self._check_map(elements, multiplicationTable)

            self.elements = elements
            self.multiplicationTable = multiplicationTable

        # orden del semigrupo, es el numero de elements en el semigrupo
        self.order = len(self.elements)

        # no se sabe si es asociativo o no
        self.isAssociative = None

        # unidad del semigrupo en la inicializacion no se sabe si la inversa
        # existe, si no existe la variable cambia a None
        self._unit = False

        # No se sabe si es conmutativo o no
        self.isConmutative = None
        # la cache para la funcion check_conmutativity, no conmutativos
        self.witnesses = None

        # cache para los inversos de un elemento x
        # inversas a derecha
        self._right_inverses = {element: None for element in elements}
        # inversas a izquierda
        self._left_inverses = {element: None for element in elements}
        # inversa a derecha e izquierda
        self._inverses = {element: None for element in elements}

        # cache para los elementos que commutator
        self._commutators = {element: None for element in elements}

    def _check_map(self, elements, table):
        """
           Esta funcion chequea si table es una table de multiplicacion
           valida. Una tabla es validad si para todo par de elementos de
           elements esta definida la operacion, ademas no puede tener
           operaciones fuera del dominio

           Parametros
           ----------
           elements: iterable con los elementos del semigrupo
           table: dict. Tabla de multiplicacion a testear

           Return
           ------
           out: True en caso de que la tabla sea correcta, se lanza un error
                en caso contrario
        """
        # la operacion esta bien definida si para todo par de elementos esta
        # definida, ademas la operacion debe ser cerrada

        # la operacion es cerrada
        for i in table.values():
            if not (i in elements):
                raise OperationOutOfDomainError()

        # el diccionario debe tener n^2 elementos, con n el numero de elementos
        # del semigrupo, las siguientes lineas no son estrictamentes necesarias
        # pero optiizan el mejor de los casos cuando hay una excepcion
        # -----------------------------------------
        # numberOfElements = len(elements)
        # if (numberOfElements ** 2) < len(table):
        #     raise ElementsWithoutOperationError()
        # if (numberOfElements ** 2) > len(table):
        #     raise MultivaluedOperation()
        # -----------------------------------------

        # cada elemento a_i debe estar operado a izquierda con los elementos
        # a_j, es decir, a_i * a_j debe tener un valor asociado

        # para cada elemento se va a crear un conjunto de elementos de la forma
        # (a_j, value) el cual representa a_i * a_j = value, cada conjunto
        # debe tener el mismo numero de elementos que hay en el semigrupo
        counter = {}
        numberOfElements = len(elements)
        for (element, operating), value in table.items():
            # solo se agregan entradas al diccionario que lleva la cuenta si
            # ambos elementos de la pareja (element, operating) estan en el
            # semigrupo
            if operating in elements and element in elements:
                # si no hay una entrada para element, se crea
                if not counter.get(element, 0):
                    counter[element] = set([(operating, value)])
                else:
                    # se agrega el par (operating, value)
                    counter[element].add((operating, value))

        # como cada elemento esta operado con los demas elementos del conjunto
        # incluyendose, entonces los conjuntos formados anteriormente tienen
        # exactamente numberOfElements elementos
        for element in elements:
            # si no esta en el diccionario, entonces no se definieron valores
            # para las parejas (element, a_j)
            if not counter.get(element, 0):
                raise ElementsWithoutOperationError()
            # si el numero de elementos con los que se relaciona element es
            # menor que el numero de elementos es porque element no se
            # relaciono con todos
            if len(counter[element]) < numberOfElements:
                raise ElementsWithoutOperationError()

        return True

    def __raises(self, subset, elements):
        """
        Esta funcion es un ayudante para _check_table, no debe ser usada en
        ninguna parte del codigo distinta a la funcion _check_table
        """

        for element in elements:
            count = subset.count(element)
            if count == 0:
                raise ElementsWithoutOperationError()
            if count >= 2:
                raise MultivaluedOperation()

    def _check_table(self, elements, table):
        """
           Esta funcion chequea si table es una table de multiplicacion
           valida. Una tabla es validad si para todo par de elementos de
           elements esta definida la operacion, ademas no puede tener
           operaciones fuera del dominio

           Parametros
           ----------
           elements: iterable con los elementos del semigrupo
           table: list. Tabla de multiplicacion a testear

           Return
           ------
           out: True en caso de que la tabla sea correcta, se lanza un error
                en caso contrario
        """
        # la operacion esta bien definida si para todo par de elementos esta
        # definida, esto esta asegurado si cada elemento aparece solo
        # una vez en la primera fila y solo una vez en la primera columna,
        # ademas la operacion debe ser cerrada

        # los elementos aparecen una vez en la fila 0
        subset = table[0][1:]
        self.__raises(subset, elements)

        # los elementos aparecen una vez en la columna 0
        subset = [table[i][0] for i in range(1, len(table))]
        self.__raises(subset, elements)

        # la operacion es cerrada
        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                if not(table[i][j] in elements):
                    raise OperationOutOfDomainError()

        return True

    def _table2map(self, table):
        """
           Esta funcion convierte la tabla de multiplicacion en formato MATRIX
           a tabla de multiplicacion en formato DICT

           Parametros
           ----------
           table: list. tabla de multiplicacion en formato MATRIX

           Return
           ------
           out: dict. tabla de multiplicaion en formato DICT
        """

        # se debe recorrer cada elemento a_i de la primera columna, y para cada
        # elemento recorrer los elementos b_i de la primera fila, formado el
        # par (a_i, b_i) que es la clave del diccionario

        tableDictFormart = {}
        numberOfElements = len(table[0])

        for i in range(1, numberOfElements):  # ciclo sobre la columna 0
            for j in range(1, numberOfElements):  # ciclo sobre la fila 0
                # se crea la entrada con la operacion en el diccionario
                tableDictFormart[(table[i][0], table[0][j])] = table[i][j]

        return tableDictFormart

    def _check_associativity(self):
        """
        Esta funcion retorna True si el semigrupo es asociativo, False en caso
        contrario
        """
        if self.isAssociative is not None:
            return self.isAssociative

        # se asume que si es asociativo
        self.isAssociative = True

        # se debe hacer cada operacion para chequear que sea asociativa,
        # entonces se debe recorrer cada elemento en (a_i * a_j) * a_k
        elements = list(self.elements)
        for i in range(self.order):
            for j in range(self.order):
                for k in range(self.order):
                    if self.op(self.op(elements[i], elements[j]), elements[k]) != self.op(elements[i], self.op(elements[j], elements[k])):
                        self.isAssociative = False
                        return self.isAssociative

        return self.isAssociative

    def op(self, x, y):
        """
        Esta realiza la operacion entre los elementos x, y del semigrupo

        Parametros
        ----------
        x: elemento con el que se quiere operar a izquierda
        y: elemento con el que se quiere operar a derecha

        Return
        ------
        out: resultado de la operacion x * y
        """
        return self.multiplicationTable[(x, y)]

    def isin(self, x):
        """
        Esta funcion verifica si el elemento x esta en el semigrupo, retorna
        True si x esta y False en caso contrario
        """

        return x in self.elements

    def has_unit(self):
        """
        Esta funcion verifica si el semigrupo tiene unidad, en caso de que
        tenga unidad la retorna, retorna False si no tiene unidad
        """
        # si la unidad existe, entonces es unica, suponga que existen 2,
        # esto es, e1, e2 entonces se tiene que e1 = e1 * e2 = e2 -> e1 = e2

        # si el semigrupo tiene unidad e, se cumple que e * e = e, entonces los
        # posibles candidatos son todos los elementos a para los que a * a = a

        # se recorren todos los elementos
        for posibleIdentity in self.elements:
            # si el elemento operado con sigo mismo da el mismo valor, entonces es un candidato
            if self.multiplicationTable[(posibleIdentity, posibleIdentity)] == posibleIdentity:
                # se mira que la posible identidad actue como tal en ambos
                # lados para todos los elementos
                for element in self.elements:
                    if self.multiplicationTable[(posibleIdentity, element)] != element:
                        break
                    if self.multiplicationTable[(element, posibleIdentity)] != element:
                        break
                else:
                    return posibleIdentity

        return False

    def unit(self):
        """
        Esta funcion retorna la unidad del semigrupo, si existe, en caso
        contrario retorna None
        """

        # si no se ha inicializado la cache
        if self._unit is False:
            self._unit = None  # se asume que ho hay unidad
            unit = self.has_unit()

            # si hay unidad se cambia el valor de self._unit
            if unit is not False:
                self._unit = unit

        return self._unit

    def check_commutativity(self, witnesses=False):
        """
        Esta funcion chequea si el semigrupo es conmutativo, un semigrupo es
        conmutativo si se cumple que (a * b) * c = a * (b * c) con a, b, c
        elementos del semigrupo

        Return
        ------
        out: True si el semigrupo es conmutativo, False en caso contrario
        """
        # primero se verifica si los resultados estan en la cache
        if self.isConmutative is not None:
            if witnesses is True:
                return self.witnesses

            return self.isConmutative

        # en caso de que no se haya inicializado la cache aun se asume que es
        # conmutativo
        self.isConmutative = True
        self.witnesses = {}

        # los set no tienen orden, para iterarlos en el mismo orden 2 veces se
        # neceta una estructura de datos que mantenga el orden
        elements = list(self.elements)

        # se recorren todos los elementos
        for i in range(self.order):
            # se recorren los elementos para chequeaer que (a * b) = (b * a)
            for j in range(i + 1, self.order):
                if self.multiplicationTable[(elements[i], elements[j])] != \
                   self.multiplicationTable[(elements[j], elements[i])]:
                    # cuando no son iguales entonces se guarda
                    self.witnesses[(elements[i], elements[j])] = self.multiplicationTable[(elements[i], elements[j])]
                    self.witnesses[(elements[j], elements[i])] = self.multiplicationTable[(elements[j], elements[i])]

        # ----------------------------------------------------------------------
        # probando algo nuevo
        # for (elementA, elementB), valueC in self.multiplicationTable.items():
        #     for (aElement, bElement), cValue in \
        #             self.multiplicationTable.items():
        #         if valueC != cValue:
        #             self.witnesses[(elementA, elementB)] = valueC
        #             self.witnesses[(aElement, bElement)] = cValue
        # ----------------------------------------------------------------------

        # si self.witnesses tienen elementos entonces no es conmutativo
        if self.witnesses:
            self.isConmutative = False
            return self.witnesses

        return self.isConmutative

    def __set_right_inverses(self, element):
        """
        Esta funcion genera todas las inversas a derecha de un elemento dado,
        esta funcion no debe ser usado por otra funcion
        """

        # Se mira si ya esta guardado en cache
        if self._right_inverses[element] is not None:
            return

        # se obtiene la unidad del semigrupo
        unit = self.unit()

        # si no hay una unidad se lanza una excepcion
        if unit is None:
            raise SemigroupWithoutUnit('''element without right inverse,
                                          semigroup has no unit''')

        # se inicializa la lista de inversas a derecha
        self._right_inverses[element] = []

        # se recorren todos los elementos a_i para verificar a * a_i = e
        for posibleInverse in self.elements:
            if self.multiplicationTable[(element, posibleInverse)] == unit:
                self._right_inverses[element].append(posibleInverse)

    def __set_left_inverses(self, element):
        """
        Esta funcion genera todas las inversas a izquierda de un elemento dado,
        esta funcion no debe ser usado por otra funcion
        """

        # Se mira si ya esta guardado en cache
        if self._left_inverses[element] is not None:
            return

        # se consigue la unidad del semigrupo
        unit = self.unit()

        # si no hay una unidad se lanza una excepcion
        if unit is None:
            raise SemigroupWithoutUnit('''element without left inverse,
                                          semigroup has no unit''')

        # se restablece el conjunto de inversas a derecha
        self._left_inverses[element] = []

        # se recorren todos los elementos a_i para verificar a_i * a = e
        for posibleInverse in self.elements:
            if self.multiplicationTable[(posibleInverse, element)] == unit:
                self._left_inverses[element].append(posibleInverse)

    def has_right_inverse(self, element):
        """
        Esta funcion retorna True si element tiene inversa a derecha, False
        en el caso contrario
        """
        # se inicializa el conjunto de inversas a derecha de element
        self.__set_right_inverses(element)
        # la lista no sea None
        hasInvert = self._right_inverses[element] is not None
        # debe tener al menos un elemento
        hasInvert = hasInvert and len(self._right_inverses[element]) > 0
        return hasInvert

    def right_inverse(self, element):
        """
        Esta funcion retorna la inversa a derecha de element(si tiene, en caso
        contrario se levanta un error), si tiene muchas inversas a derecha, se
        retornara una aleatoria
        """
        # se inicializa el conjunto de inversas a derecha de element
        self.__set_right_inverses(element)

        # si no tiene inversa a derecha se lanza una excepcion
        if len(self._right_inverses[element]) == 0:
            raise ElementWithoutInverse(RIGHT)

        # se escoje una al azar
        return choice(self._right_inverses[element])

    def right_inverses(self, element):
        """Esta funcion retorna todas las inversas de a derecha de element(si
        tiene, en caso contrario se levanta un error)
        """
        # se inicializa el conjunto de inversas a derecha de element
        self.__set_right_inverses(element)

        # si no tiene inversa a derecha se lanza una excepcion
        if len(self._right_inverses[element]) == 0:
            raise ElementWithoutInverse(RIGHT)

        # se etornan todas las inversas
        return self._right_inverses[element]

    def has_left_inverse(self, element):
        """
        Esta funcion retorna True si element tiene inversa a izquierda, False
        en el caso contrario
        """
        # se inicializa el conjunto de inversas a izquierda de element
        self.__set_left_inverses(element)
        # la lista no sea None
        hasInvert = self._left_inverses[element] is not None
        # debe tener al menos un elemento
        hasInvert = hasInvert and len(self._left_inverses[element]) > 0
        return hasInvert

    def left_inverse(self, element):
        """
        Esta funcion retorna la inversa a izquierda de element(si tiene, en
        casocontrario se levanta un error), si tiene muchas inversas a
        izquierda, se retornara una aleatoria
        """
        # se inicializa el conjunto de inversas a izquierda de element
        self.__set_left_inverses(element)

        # si no tiene inversa a izquierda se lanza una excepcion
        if len(self._left_inverses[element]) == 0:
            raise ElementWithoutInverse(LEFT)

        # se escoje una al azar
        return choice(self._left_inverses[element])

    def left_inverses(self, element):
        """
        Esta funcion retorna todas las inversas a izquierda de element(si
        tiene, en caso contrario se levanta un error)
        """
        # se inicializa el conjunto de inversas a derecha de element
        self.__set_left_inverses(element)

        # si no tiene inversa a derecha se lanza una excepcion
        if len(self._left_inverses[element]) == 0:
            raise ElementWithoutInverse(LEFT)

        # se retornan todas las inversas
        return self._left_inverses[element]

    def has_inverse(self, element):
        """
        Esta funcion retorna True si element tiene inversa y False en caso
        contrario
        """
        # si a tiene inversa a izquierda y a derecha, esto es, a * c = e y
        # b * a = e, entonces se cumple que b = c, pues,
        # b = b * e = b * a * c = e * c = c
        return self.has_left_inverse(element) and self.has_right_inverse(element)

    def inverse(self, element):
        """
        Esta funcion retorna la inversa de element, si la tiene, y False en el
        caso contrario
        """
        if self.has_inverse(element):
            return self._right_inverses[element][0]

    def commutators(self, element):
        """
        Esta funcion retorna los elementos que comutan con element
        """
        # se mira primero en cache
        if self._commutators[element] is not None:
            return self._commutators[element]

        # si el semigrupo es conmutativo entonces todos los elementos conmutan
        # con todos
        if self.check_commutativity():
            self._commutators[element] = self.elements
            return self.elements

        # si no es conmutativo se necesita recorrer todos los elementos e ir
        # chequeando
        self._commutators[element] = []

        for elem in self.elements:
            # si conmutan se agrega a la lista
            if self.op(element, elem) == self.op(elem, element):
                self._commutators[element].append(elem)

        return self._commutators[element]


def main():
    pass


if __name__ == '__main__':
    main()
