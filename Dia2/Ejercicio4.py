## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯
##Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor y el menor de todos estos números.

grandecito = 0
pequenito = 0

for i in range (1 , 10):
    numerito= int(input("Ingresa el numero: "))

    if i == 1:

        grandecito= numerito
        pequenito= numerito

## la variable elif= se utiliza para especificar condiciones adicionales que se deben verificar después de la sentencia "if
    elif numerito > grandecito :
            grandecito= numerito

    elif numerito < pequenito :
            pequenito = numerito 

print ("Grandecito= ", grandecito)
print ("Pequeñito= ", pequenito)

## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯