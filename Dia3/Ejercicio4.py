## Ejercicio -4 [Aura Pico] cc: 1097498480 👨‍🦯

## Create a function that generates a random password of a given length.
# Ensure it includes uppercase letters, lowercase letters, numbers, and symbols.
#  Add an option to exclude specific characters or enforce minimum requirements for each type of character.

import random
import string

def generate_password(length=12, exclude_chars='', min_upper=1, min_lower=1, min_digits=1, min_symbols=1):
    """Genera una contraseña aleatoria con los requisitos especificados."""
    
    # Definir los conjuntos de caracteres
    upper = set(string.ascii_uppercase) - set(exclude_chars)
    lower = set(string.ascii_lowercase) - set(exclude_chars)
    digits = set(string.digits) - set(exclude_chars)
    symbols = set(string.punctuation) - set(exclude_chars)
    
    # Garantizar que la longitud sea suficiente
    min_required = min_upper + min_lower + min_digits + min_symbols
    if length < min_required:
        raise ValueError(f"La longitud mínima permitida es {min_required} para cumplir con los requisitos.")
    
    # Generar los caracteres requeridos
    password = (
        random.sample(upper, min_upper) +
        random.sample(lower, min_lower) +
        random.sample(digits, min_digits) +
        random.sample(symbols, min_symbols)
    )
    
    # Completar la contraseña con caracteres aleatorios
    all_chars = list(upper | lower | digits | symbols)
    password += random.choices(all_chars, k=length - min_required)
    
    # Mezclar la contraseña para mayor aleatoriedad
    random.shuffle(password)
    
    return ''.join(password)

# Solicitar datos al usuario
length = int(input("Ingrese la longitud de la contraseña: "))
exclude_chars = input("Ingrese caracteres a excluir (opcional): ")

# Generar y mostrar la contraseña
password = generate_password(length, exclude_chars)
print("Contraseña generada:", password)

## Ejercicio -4 [Aura Pico] cc: 1097498480 👨‍🦯<3