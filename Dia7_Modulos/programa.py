from mi_modulo import *

print (sumar(5,6) )

print (restar(8,4) )

print (multiplicar(7 , 8) )

print (unirListas([1,2,3,4], [5,6,7,8]))

print(multiRestar(9,6))


estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Álvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Méndez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragán",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejía",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Pérez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos García",
    "Vladimir Díaz Contreras"
]

recorrerLista(estudiantes)
obtenerEstudiantes = obtenerEstudiantes (estudiantes , 10)
print(obtenerEstudiantes)
modificarEstudiantes(estudiantes, 31 , "Pedro felipe gomez")
recorrerLista(estudiantes)