"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    listaEnteros = []                           #inicializo lista enteros
    listaStrings = []                           #inicializo lista strings

    for i in lista:                             #para cada elemento de la lista
        if (isinstance(i, int) ):               #compruebo que el tipo del elemento sea int
            listaEnteros.append(i)              #si es int, lo agrego en listaEnteros
        else:                                   #sino
            listaStrings.append(i)              #lo agrego en listaString
    
    
    listaUnida = listaStrings + listaEnteros    #uno las listas
    return listaUnida                           #devuelvo la listaUnida


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    listaEnteros = [int(i) for i in lista if isinstance(i, int)]  #genero una nueva lista de compresion con solo los enteros
    listaStrings = [i for i in lista if isinstance(i, str)]       #genero una nueva lista de compresion con solo los strings

    listaUnida = []                                               #instancia nueva lista
    listaUnida.extend(listaStrings)                               #le agrego la lista string
    listaUnida.extend(listaEnteros)                               #le agrego la lista de enteros

    return  listaUnida                                            #devuelvo la listaUnida


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    def isint(i: Union[float, str]):    #defino funcion isint para usarla como key y customizar la funcion sorted
        return isinstance(i, int)       #la funcion recibe un elemento y devuelve true si es int, false si no es

    return sorted(lista, key = isint)   #ordeno la lista con la key customizada(), me va ordenar la lista con los numeros al final
     

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    def isint(i):                      # Primero declaramos una función condicional
       return  isinstance(i, int)      # Sólo devolvemos True si el elemento es int
    def isstr(i):                      # Primero declaramos una función condicional
       return  isinstance(i, str)      #Sólo devolvemos True si el elemento es str


    
    listaEnteros = filter(isint, lista)  #genero una nueva lista filtrada con solo los enteros
    listaStrings = filter(isstr, lista)  #genero una nueva lista fitlrada con solo los strings

    listaUnida = []                       #instancia nueva lista
    listaUnida.extend(listaStrings)       #le agrego la lista string
    listaUnida.extend(listaEnteros)       #le agrego la lista de enteros
    return listaUnida                     #devuelvo la listaUnida

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
