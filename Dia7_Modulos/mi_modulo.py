def sumar (a , b):
    return a+b

def restar ( a, b):
    return a-b

def multiplicar (a , b ):
    return a*b


def unirListas(a , b):
    ListaNueva = a
    ListaNueva.extend (b)
    return ListaNueva

def multiRestar (a, b):
    resultado = multiplicar ( a, b) - ( a- b)
    return resultado