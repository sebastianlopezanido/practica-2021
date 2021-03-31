"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    


    if posFinal % 2 == 0 and palabra[0:posMedio] == palabra[posMedio:posFinal][::-1]:  #si la cantidad de letras es par y la primera mitdad es igual al inverso de la segunda mitad
        return True                                                                    #es palindromo
    if posFinal % 2 == 1 and palabra[0:(posMedio)] == palabra[(posMedio+1):posFinal][::-1]: #si la cantidad de letras es par y la primera mitdad es igual al inverso de la segunda mitad
        return True                                                                    #es palindromo
    return False                                                                       #no es palindromo



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
    posFinal = len(palabra) #posicion final del str
    posMedio = int(posFinal / 2) #posicion media del str


    if posFinal % 2 == 0 and palabra[0:posMedio] == palabra[posMedio:posFinal][::-1]:  #si la cantidad de letras es par y la primera mitdad es igual al inverso de la segunda mitad
        return True                                                                    #es palindromo
    if posFinal % 2 == 1 and palabra[0:(posMedio)] == palabra[(posMedio+1):posFinal][::-1]: #si la cantidad de letras es par y la primera mitdad es igual al inverso de la segunda mitad
        return True                                                                    #es palindromo
    return False                                                                       #no es palindromo



# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
