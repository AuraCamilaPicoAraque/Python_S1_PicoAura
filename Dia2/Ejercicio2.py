## Ejercicio -2 [Aura Pico] cc: 1097498480 👨‍🦯
## Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado de la siguiente serie:

def calcular_serie(N):
    # Inicializamos la suma de la serie
    suma = 0.0
    
    # Recorremos desde 1 hasta N
    for i in range(1, N + 1):
        if i == 1:
            suma += 1  # primer término
        else:
            suma += 1 / i  # términos restantes
    
    # Restamos el segundo término
    suma -= 1 / 2
    
    return suma

def main():

    N = int(input("Ingrese un número entero N: "))
    
    if N < 1:
        print("N debe ser un número entero mayor o igual a 1.")
        return
    
    resultado = calcular_serie(N)
    
    # cantidad de términos y el resultado
    cantidad_terminos = N 
    print(f"Cantidad de términos: {cantidad_terminos}")
    print(f"Resultado de la serie: {resultado}")


if __name__ == "__main__":
    main()


## Ejercicio -2 [Aura Pico] cc: 1097498480 👨‍🦯