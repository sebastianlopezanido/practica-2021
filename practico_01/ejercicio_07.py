"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    if palabra == palabra[::-1]:    #Comparo la palabra con su inversa
        return True                 #Si son iguales devuelvo True
    return False                    #Si son distintos devuelvo False

# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    posFinal = len(palabra)          #posicion final del str
    posMedio = int(posFinal / 2)     #posicion media del str

    if posFinal % 2 == 1:            #Me fijo si la longitud es par o impar
        posMedio += 1                #Si es impar le sumo 1 a la posicion media del str
    return palabra[:posMedio]        #Devuelvo el principio de la palabra hasta la posicion media del str   
        


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
