## Ejercicio - MODULOS [Aura Pico] cc: 1097498480 👨‍🦯

from modulo import *

nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

## Aqui ponemos las funciones que nos pide el usuario sea ai si queremos editar o ver un estudiante

def agregar ():
        n1=input("ingrese el primer nombre del estudiante")
        n2=input("ingrese el segundo nombre (si lo tiene)")

        ap1=input("Ingrese el primer apellido")
        ap2=input("ingrese el segundo apellido")

        nombres.append([n1,n2])
        apellidos.append([ap1,ap2])

def ver ():
        
        c1 = 0
        c = 0

        for i in range(len(nombres)):
            ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
            print("estudiante#",i+1," "," ".join(nombres[c1])," ".join(apellidos[c]))
            c1+=1
            c+=1

def edit ():
            
            ## porque coloco el ver () esto porque ya tenemos una funcion que nos muestra la lista lo que nos facilita el estar copiando y pegando
            ver ()

            edt=int(input("Ingrese el estudiante que quiere editar (el numero de la lista):  "))
            if 0 <= edt < len(nombres):

                print("Seleccione qué desea editar:  ")
                print("1. Primer nombre\n2. Segundo nombre\n3. Primer apellido\n4. Segundo apellido")

                opc = int (input(": "))
                opciones = input ("Ingresa el nuevo nombre o apellido:  ")

## Aqui editamos el nombre....
                if opc == 1 :
                      nombres[edt-1][0]=(opciones)

## Porque pongo "and len(nombres[edt])>1 :"  esto es para comprobar en la lista si el estudiante tiene un segundo nombre si no es asi te vota error 
                elif opc == 2 and len(nombres[edt])>1 :
                      nombres[edt-1][1]= (opciones)     

## Y aqui editamos el apellido....
                elif opc == 3 :
                       apellidos[edt-1][0]= (opciones)   

                elif opc == 4 :
                      apellidos[edt-1][1]= (opciones)   



                else:
                       print("La opcion que pusiste no esta disponible ~~")
            else: 
                   print("Numero de estudiante no encontrado ~~~")
   
def eli ():
            
            ver ()
            el=int(input("ingrese el estudiante que quiere eliminar (el numero de la lista):  "))
            nombres.pop(el-1)
            apellidos.pop(el-1)

            print("Estudiante eliminado exitosamente ;) ~~~")
       
def exit ():
        print("~~~~~~ Saliendo de programa ~~~~~~~")
        

## Ejercicio - MODULOS [Aura Pico] cc: 1097498480 👨‍🦯