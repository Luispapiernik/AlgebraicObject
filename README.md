# AlgebraicObject
Programación de algunos objetos algebraicos finitos(semigrupos, monoides, grupos,...)

## Enunciado

Crea una clase que encapsule las propiedades de un semigrupo finito (algebraico):

Al inicializarse hay que pasarle los elementos del semigrupo, el ‘nombre’ del semigrupo y la tabla de multiplicación de estos. La signatura de la tabla de multiplicación se puede proveer en diferentes formatos:

    - Diccionario cuyas claves son pares de elementos y el valor es el resultado de la multiplicación. 
    - Array dos dimensional con la tabla de multiplicación.

El formato se indica con un parámetro llamado format, el cual tiene un valor por defecto decidido por ustedes (con algo de criterio).

En todo caso, cuando se inicializa el semigrupo, se chequea que para todo par de elementos del semigrupo esté definida la operación. Y se puede establecer un warning si la tabla en formato diccionario tiene ‘operaciones’ por fuera del dominio. Ahora, independientemente del formato en que se inicialice el semigrupo, podemos mantener internamente en la clase el diccionario de operaciones ya que es más simple realizar operaciones con él.

    Tiene una función interna llamada _table2map para convertir tabla multiplicativa a diccionario.
    Tiene una funciòn _check_table para chequear que la tabla sea correcta.
    Tiene una funciòn _check_map para chequear que el diccionario de operaciones sea correcto.
    Tiene una función interna llamada _check_associativity para chequear la asociatividad en la tabla.

En caso de error levantar **errores apropiados**

Por ahora vamos a adicionar los siguientes métodos

Algunos de los métodos son los siguientes (cambiar los nombres a gusto):

op(x, y): Realiza la operación entre x y y (elementos del semigrupo).

isin(x): Verifica si x pertenece al semigrupo

has_unit(): Verifica si el semigrupo tiene unidad. Esta funcion tiene una cache.

unit(): Retorna la unidad del semigrupo. ¿Por qué es única? Esta funcion tiene una cache.

check_commutativity(witnesses=False): Verifica si el semigrupo es abeliano o no. Esta función tiene una caché. Si 
witnesses=True, retorna todos los testigos que verifican la no conmutatividad.

has_right_inverse(x): Verifica si x tiene inversa a derecha. Esta función tiene una caché.

right_inverse(x, seed=None): Retorna alguna inversa a derecha de x. Si tiene varias inversas, retorna una de ellas aleatoriamente. Esta función tiene una caché.

right_inverses(x): Retorna todas las inversas a derecha de x. Esta función tiene una caché.
De manera analoga, has_left_inverse, left_inverse y left_inverses.
También, has_inverse e inverse (¿por qué no hay funciòn inverses?)

Las funciones relacionadas con invertibilidad levantan un error apropiado en caso que no exista unidad en el semigrupo.

commutators(x): Retorna los elementos que conmutan con x. Esta función tiene una caché. (y es muy eficiente si ya supieramos que el semigrupo es conmutativo).

left_cancellable(x): Retorna True si x es cancelable a izquierda. 
De la misma manera, agregue right_cancellable y cancellable. Tenga en cuenta que si el semigrupo tiene unidad, cancelable a derecha o izquierda es equivalente a  invertible.

Cree ahora la subclase monoid y la subclase group. Progresivamente, particularice el código de algunos de los métodos anteriores usando las propiedades específicas de cada caso.

