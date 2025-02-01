## Ejercicio -3 [Aura Pico] cc: 1097498480 👨‍🦯

## Create a function that checks whether a number is even or odd.
# Extend it to classify numbers as prime or composite.
# Modify it to check if a number is a perfect square.


import math

def clasificacion(n):
    result = {}
    # Verificar si es par o impar
    result['paridad'] = "Par" if n % 2 == 0 else "Impar"
    
    # Verificar si es primo o compuesto
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                result['tipo'] = "Compuesto"
                break
        else:
            result['tipo'] = "Primo"
    else:
        result['tipo'] = "Ni primo ni compuesto"
    
    # Verificar si es un cuadrado perfecto
    result['cuadrado_perfecto'] = "Sí" if math.isqrt(n) ** 2 == n else "No"
    
    return result

# Solicitar un número al usuario
num = int(input("Ingrese un número: "))
num_info = clasificacion(num)

# Mostrar resultados
print(f"El número {num} es {num_info['paridad']}, {num_info['tipo']}, y {'' if num_info['cuadrado_perfecto'] == 'Sí' else 'no '}es un cuadrado perfecto.")

## Ejercicio -3 [Aura Pico] cc: 1097498480 👨‍🦯