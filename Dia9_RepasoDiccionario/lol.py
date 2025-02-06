import json
from os import system
##  Abrir
def abrirJSON ():
    Abrirlol = {}
    with open("./lol.json" , "r") as openFile :
        Abrirlol = json.load (openFile)
    return Abrirlol
    

## Guardar

def guardarJSON (lool):
    with open ("./lol.json" , "w") as outFile :
        json.dump (lool , outFile)
        
lolcito={}
booleanito = True
while (booleanito == True):
    
    lolcito=json
    print("##############################################################")
    print ("------- Bienvenidos a las clasificatorias del lol. ----------")
    print("##############################################################")
    print("\nQue te gustaría hacer?")
    print("1- Agregar un nuevo grupo para la clasificaciones.")
    print("2- Ver los grupos de la clasificacion.")
    print("3- editar un grupo. ")
    print("4- ruleta para asignar los dos grupos a competir")

    opc = int(input(": "))
    system("clear")

    if opc == 1 :
        print("Recuerda que solo son 5 integrantes ~~~~")


        nombre=input("ingrese el nombre del equipo:  ")
        region=input("ingrese la region en donde esta tu equipo:  ")

        for i in range (5):

            nomIn=input("ingrese el primer nombre del integrante:  ")
            apeIn=input("Ingrese el primer apellido del integrante:  ")
            edad= input("Ingrese la edad del integrante:  ")


            print("¿Que posicion llevara el integrante: ")
            print(" 1- Top")
            print("2- JUNGLA")
            print("3- MID")
            print("4- ADC")
            print("5- SUPPORT")

            opP = int(input(": "))
            if opP == 1:
                print("llevas TOP")
            elif opP == 2:
                print("llevas JUNGLA")
            elif opP == 3:
                print("llevas MID")
            elif opP == 4:
                print("llevas ADC")
            elif opP == 5:
                print("llevas SUPPORT")
            else:
                print("no hay posicion 6 ._. ")
            system("clear")
            guardarJSON (lolcito)