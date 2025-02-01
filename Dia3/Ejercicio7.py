## Ejercicio -7 [Aura Pico] cc: 1097498480 👨‍🦯

#Create a function to calculate the factorial of a given number.
#Extend it to calculate combinations (nCr) and permutations (nPr).
#Ensure it handles edge cases like negative numbers.

import math

def factorial(n):
    """Calcula el factorial de un número dado."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return 1 if n == 0 else math.prod(range(1, n + 1))

def combinations(n, r):
    """Calcula el número de combinaciones (nCr)."""
    if r > n or n < 0 or r < 0:
        raise ValueError("Valores inválidos para combinaciones.")
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutations(n, r):
    """Calcula el número de permutaciones (nPr)."""
    if r > n or n < 0 or r < 0:
        raise ValueError("Valores inválidos para permutaciones.")
    return factorial(n) // factorial(n - r)

# Solicitar datos al usuario
n = int(input("Ingrese un número para calcular el factorial: "))
r = int(input("Ingrese el valor de r para combinaciones y permutaciones: "))

# Calcular y mostrar resultados
print(f"Factorial de {n}: {factorial(n)}")
print(f"Combinaciones ({n}C{r}): {combinations(n, r)}")
print(f"Permutaciones ({n}P{r}): {permutations(n, r)}")


## Ejercicio -7 [Aura Pico] cc: 1097498480 👨‍🦯