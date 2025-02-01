## Ejercicio -5 [Aura Pico] cc: 1097498480 👨‍🦯

##Create a function to check if a word or phrase is a palindrome. 
# Extend it to ignore punctuation and special characters.
#  Modify it to handle multi-word palindromes.

def is_palindrome(text):
    """Verifica si una palabra o frase es un palíndromo, ignorando puntuación y espacios."""
    # Eliminar espacios y puntuación
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Verificar si es un palíndromo
    return cleaned_text == cleaned_text[::-1]

# Solicitar entrada al usuario
text = input("Ingrese una palabra o frase: ")

# Comprobar y mostrar el resultado
if is_palindrome(text):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

    

## Ejercicio -5 [Aura Pico] cc: 1097498480 👨‍🦯