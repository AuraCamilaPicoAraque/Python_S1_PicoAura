## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯

##Mostrar en pantalla si dos números enteros positivos n1 y n2 son amigos. Los números amigos son pares de números enteros positivos en los cuales la suma de los divisores propios de cada número es igual al otro número. 
##En otras palabras, dos números amigos cumplen la condición de que la suma delos divisores propios de uno de ellos es igual al otro número, y viceversa. Por ejemplo, el par de números (220, 284) es un par de números amigos. Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110. Si sumamos estos números, obtenemos 284, que es el segundo número del par.
##Por otro lado, los divisores propios de 284 son 1, 2, 4, 71 y 142, y si los sumamos, obtenemos 220, que es el primer número del par.

n1= int (input("Ingrese n1= "))
n2= int (input("Ingrese n2= "))

suma1 = 0
suma2 = 0

for i in range (1, n1-1):
    if n1 % i == 0 :
        suma1 = suma1 + i

for i in range (1, n2-1):
    if n2 % i == 0 :
        suma2 = suma2 + i


if suma1 == n2 and suma2 == n1 :
    print ("son numeros parceritos" )

else:
    print ("no son numeros parceritos")

## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯