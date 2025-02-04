## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯

##La empresa ACME desea calcular el valor de la nómina de N empleados (estos N empleados soningresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partirdel valor de la hora y la cantidad de horas trabajadas. 
##A esto se le descuenta el valor de la EPS que esel 4%, el valor de la Pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Porcada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor delsueldo Neto. 
##Para este ejercicio el valor de la hora es $20.000.Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, Pensión y salarios netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos netos.

nombreMayor = ""
nombreMenor = ""
nombre =""
mayorS = 0
menorS = 0
neto = 0
bruto = 0
eps = 0
pension = 0
promedioBruto = 0
promedioNeto= 0
totalbruto=0
totalEps=0
totalNeto=0
totalPension=0




N =  int(input("Ingresa la cantidad de empleados: "))
for i in range (N):
    nombre=(input("Nombre del empleado "  ))
    horas =int(input("Ingrese las horas de trabajadas: " ))

    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    totalbruto = totalbruto + bruto
    totalEps = totalEps + eps
    totalPension = totalPension + pension
    totalNeto = totalNeto + neto
    print ("Empleado ", nombre)
    print ("SUeldo Bruto. $" , bruto)
    print ("Eps: $ " , eps)
    print ("Pension: $ " , pension)
    print ("Sueldo Neto: $ " , neto)
    mayorS=neto

    if mayorS>menorS :
        menorS=mayorS 
        ms=mayorS

        nombreMayor = nombre
    else:
        if mayorS < menorS :
            menorS = mayorS
            nombreMenor = nombre



promedioBruto = totalbruto / N 
promedioNeto = totalNeto / N

print ("-------- Totales------ ")
print ("Total Salario Brutos: $ ", totalbruto)
print ("Total EPS: $ ", totalEps)
print ("Total Pension: $ ",totalPension)
print ("Tota Salarios Netos: $", totalNeto)
print ("Empleado que mas gana: ", nombreMayor)
print ("Empleado que menos gana: ",nombreMenor)
print ("Promedio Salarios Brutos: $", promedioBruto)
print ("Promedio Salarios Neto: $", promedioNeto)


## Ejercicio -1 [Aura Pico] cc: 1097498480 👨‍🦯