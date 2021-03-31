"""Bucle FOR y Reduce."""

from typing import Iterable


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númreos. Si
    la lista está vacia debe devolver 0.

    Restricciones: No usar bibliotecas auxiliares (Numpy, math, pandas).
    """
   
    product = 1.0               #inicializo la variable que va a dcontener el producto de todos los numeros, arranca en 1 
    count = 0                   #inicializo la variable que va a contar la cantidad de elementos de la lista, arranca en 0
    for i in numeros:           #para cada elemento "i" en numeros
        product = product * i   #el producto es igual al producto por el numero "i"
        count =+ 1              #la cantidad aumenta 1 en 1
    if count == 0:              #si no hay elementos devuelvo 0
        return 0
    return product              #sino devuelvo el producto
    

    
        



# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_basico(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce


def multiplicar_reduce(numeros: Iterable[float]) -> float:
    """CHALLENGE OPCIONAL - Re-escribir utilizando reduce.
    Referencia: https://docs.python.org/3.8/library/functools.html#functools.reduce
    """
    def counting(a, b):                 #funcion usada para contar con reduce
        return a + 1    

    def multiply (a, b):                #funcion usada para multiplicar con reduce
        return a * b
    
    count = reduce(counting, numeros,0) #llamo al reduce con la funcion counting, la lista numeros, que se inicialice en 0 y guardo el resultado en count
    if count == 0:                      #si count es 0 devuelvo 0
        return 0    
                                         #sino
    product = reduce(multiply, numeros,1)#llamo al reduce con la funcion multiply , la lista numeros, que se inicialice en 1 y guardo el resultado en product
    return product                       #devuelvo el producto
    


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN
