## Ejercicio -8 [Aura Pico] cc: 1097498480 👨‍🦯

#Create a function that counts the number of vowels and consonants in a string.
#Modify it to also count digits and special characters.
#Extend it to return the most frequently occurring character.

import string
from collections import Counter

def analyze_string(text):
    """Analiza una cadena y cuenta vocales, consonantes, dígitos y caracteres especiales."""
    vowels = "aeiouAEIOU"
    digits = string.digits
    special_chars = string.punctuation
    
    counts = {
        "vocales": sum(1 for char in text if char in vowels),
        "consonantes": sum(1 for char in text if char.isalpha() and char not in vowels),
        "dígitos": sum(1 for char in text if char in digits),
        "caracteres_especiales": sum(1 for char in text if char in special_chars)
    }
    
    # Encontrar el carácter más frecuente
    text_cleaned = [char for char in text if char.isalnum()]
    most_common_char = Counter(text_cleaned).most_common(1)
    counts["caracter_mas_frecuente"] = most_common_char[0][0] if most_common_char else None
    
    return counts

# Solicitar entrada al usuario
text = input("Ingrese un texto para analizar: ")

# Analizar la cadena y mostrar resultados
result = analyze_string(text)
print("Análisis del texto:")
print(f"Vocales: {result['vocales']}")
print(f"Consonantes: {result['consonantes']}")
print(f"Dígitos: {result['dígitos']}")
print(f"Caracteres especiales: {result['caracteres_especiales']}")
print(f"Carácter más frecuente: {result['caracter_mas_frecuente']}")


## Ejercicio -8 [Aura Pico] cc: 1097498480 👨‍🦯