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

def recorrerLista (a , b):
    for i in range (len(a)):
        print("Estudiantes # " , i + 1 , ":" , a (i) )

def obtenerEstudiantes ( a , b ):
    return a [b -1]

def modificarEstudiantes (a , b , c) :
    a [b-1] = c
    if (a[b-1]):
        return True
    else:
        return False