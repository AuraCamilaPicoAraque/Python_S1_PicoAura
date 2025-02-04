## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯
## Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado de la siguiente serie:


cantidad= int(input("La cantidad de terminos son: "))
sumatoria=0
for i in range (1, cantidad+1):
    if i% 2 == 0:
        sumatoria=sumatoria-(1/i)

## la variable elif= se utiliza para especificar condiciones adicionales que se deben verificar después de la sentencia "if {es como decir el SiNo}
    else:
        sumatoria=sumatoria+(1/i)

(print ("La sumatoria dio: ", sumatoria))



## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯