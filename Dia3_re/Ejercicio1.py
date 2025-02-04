## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯

##  Temperature Conversion
## Create a function that converts temperature from Celsius to Fahrenheit.Modify the function to also convert Fahrenheit to Celsius. Ensure the function can handle invalid inputs gracefully


def temperatura_c (grados):
    conver = (grados*9/5)+32
    return conver

## para convertir C a F cogimosla formula convencional de (grados* 9/5)+32 y ese resultado sera enviado a conver y lo llevara a la variable de farhe

def temperatura_f (farhe):
    conver2 = (farhe-32)*5/9
    return conver2

print ("Que opcion quieres convertir? ")
print ("Grado Celsius = (1)")
print ("Farhenheit = (2) ")

## Para hacer las opciones que quiera elegir el ususario , utilizamos la opcion if y le damos el valor de num1 al que si elejimos 1 va a ser celsus y si elegimos 2 sera farhenheit , al ususario colocar otro que no este registrado le votara que laopcion es invalida

num1=int(input ("Ingresa la opcion que deseas:"))

if num1 == 1 :
    grados=int(input ("Ingresa el numero a convertir de grados a farhe :"))
    print(temperatura_c(grados), "º F ")


if num1 == 2 :
    farhe=int(input ("Ingresa el numero a convertir de farhe a grados :"))
    print(temperatura_c(farhe), "º G ")


if num1 > 2 :
    print ("numero de opcion invalido")


## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯