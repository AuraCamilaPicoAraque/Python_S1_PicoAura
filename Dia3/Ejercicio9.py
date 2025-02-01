## Ejercicio -9 [Aura Pico] cc: 1097498480 👨‍🦯

#Write a function to validate an email address format.
#Extend it to validate phone numbers based on a given country format.
#Modify it to check if a given password meets security requirements.



import re

# Función para validar una dirección de correo electrónico
def validar_email(email):
    # Expresión regular para validar el correo electrónico
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_email, email):
        return True
    else:
        return False

# Función para validar un número de teléfono según un formato específico
def validar_telefono(telefono, pais='MX'):
    if pais == 'MX':
        # Formato de teléfono mexicano (XXX-XXX-XXXX)
        patron_telefono = r'^\d{3}-\d{3}-\d{4}$'
        if re.match(patron_telefono, telefono):
            return True
    # Puedes agregar más países y formatos aquí
    return False

# Función para validar la seguridad de una contraseña
def validar_contraseña(contraseña):
    # La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula, un número y un carácter especial
    patron_contraseña = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~]).{8,}$'
    if re.match(patron_contraseña, contraseña):
        return True
    else:
        return False

# Ejemplo de uso de las funciones:
email = "test@ejemplo.com"
telefono = "123-456-7890"
contraseña = "Contraseña123!"

print("Email válido:", validar_email(email))  # True o False
print("Teléfono válido:", validar_telefono(telefono))  # True o False
print("Contraseña válida:", validar_contraseña(contraseña))  # True o False


## Ejercicio -9 [Aura Pico] cc: 1097498480 👨‍🦯