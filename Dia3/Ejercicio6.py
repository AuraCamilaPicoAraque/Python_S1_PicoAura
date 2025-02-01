## Ejercicio -6 [Aura Pico] cc: 1097498480 👨‍🦯

##Write a function to generate the Fibonacci sequence up to a given number of terms.
# Modify it to return only even Fibonacci numbers.
# Extend it to find the sum of Fibonacci numbers within a specified range.


def fibonacci_sequence(n):
    """Genera la secuencia de Fibonacci hasta n términos."""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def even_fibonacci(n):
    """Retorna solo los números pares de la secuencia de Fibonacci hasta n términos."""
    return [num for num in fibonacci_sequence(n) if num % 2 == 0]

def sum_fibonacci_range(start, end):
    """Calcula la suma de los números de Fibonacci dentro de un rango especificado."""
    sequence = []
    a, b = 0, 1
    while a <= end:
        if a >= start:
            sequence.append(a)
        a, b = b, a + b
    return sum(sequence)

# Solicitar datos al usuario
n = int(input("Ingrese el número de términos de Fibonacci: "))
start = int(input("Ingrese el inicio del rango para la suma: "))
end = int(input("Ingrese el fin del rango para la suma: "))

# Generar y mostrar resultados
print("Secuencia de Fibonacci:", fibonacci_sequence(n))
print("Números pares en la secuencia:", even_fibonacci(n))
print(f"Suma de Fibonacci en el rango {start}-{end}:", sum_fibonacci_range(start, end))


## Ejercicio -7 [Aura Pico] cc: 1097498480 👨‍🦯