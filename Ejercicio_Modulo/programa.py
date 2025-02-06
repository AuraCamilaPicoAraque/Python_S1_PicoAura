## Ejercicio - MODULOS [Aura Pico] cc: 1097498480 👨‍🦯

import modulo
## Sirve para que tengan una coorelacion el modulo.py y yo pueda utilizar las variables de la funcion modulo.(nombre) () 

booleanito = True
while booleanito ==True:

    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    
    opc = int(input(":"))

## Lo que hago aqui es poner las variables de [def (nombre) ()] que indica lo que nosotros como usuario vamos a seleccionar 

    if opc == 1:
        modulo.agregar()

    elif opc == 2 :
        modulo.ver ()

    elif opc == 3 :
        modulo.edit ()
        
    elif opc == 4 :
        modulo.eli ()

    elif opc == 5 :
        modulo.exit ()
        break
    
    else:
        print("Opción incorrecta, intenta de nuevo.")
        
        
## Ejercicio - MODULOS [Aura Pico] cc: 1097498480 👨‍🦯