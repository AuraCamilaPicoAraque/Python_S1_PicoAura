

def suma_divisores_propios(n):
    suma = 0
    for i in range (1 , n ):
        if n% i == 0:
            suma += i #suma=suma+i
    return suma


def numeros_amigos(a,b):
    return suma_divisores_propios(a) == b and suma_divisores_propios(b) == a

num1=int(input ("INgresa el primer numero:"))
num2=int(input ("INgresa el segundo numero:"))

if (numeros_amigos(num1, num2)):
    print("Los numeros son parceros")
else:
    print("Los numeros se odian")