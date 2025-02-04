#Recorrer una lista
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

booleanito= True
while (booleanito==True):


    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Editar  nombre de estudiante")
    print("2.Editar  apellido de estudiante")
    print("3.Eliminar estudiante")
    print("4.Salir del programa")


    opcionUsuario= int(input(":"))
    if(opcionUsuario==1):
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            print("Estudiante #",i+1,": ",nombres[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        nombres[numeroEstudiante-1]=nombreEstudianteNuevo



        for i in range(len(nombres)):
                print("Estudiante #",i+1,": ", nombres[i])


    elif(opcionUsuario==4):
        booleanito== False
        break

    elif(opcionUsuario==2):
        print("Lista de estudiantes:")
        for i in range(len(apellidos)):
            print("Estudiante #",i+1,": ",apellidos[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el apellido nuevo del estudiante?:")
        apellidos[numeroEstudiante-1]=nombreEstudianteNuevo

    elif(opcionUsuario==3):
        print("Lista de estudiantes:")
        for i in range(len(nombres , apellidos)):
            print("Estudiante #",i+1,": ",nombres , [i])
        numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
        nombres.pop(nombres , apellidos-1)

