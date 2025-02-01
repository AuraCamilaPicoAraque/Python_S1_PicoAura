## Ejercicio -10 [Aura Pico] cc: 1097498480 👨‍🦯

#Implement a function that sorts a list using bubble sort.
#Extend it to implement selection sort and insertion sort.
#Modify it to allow sorting in both ascending and descending order.


def bubble_sort(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascendente and lista[j] > lista[j+1]) or (not ascendente and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Selection Sort
def selection_sort(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        # Encuentra el mínimo o máximo dependiendo del orden
        indice_extremo = i
        for j in range(i+1, n):
            if (ascendente and lista[j] < lista[indice_extremo]) or (not ascendente and lista[j] > lista[indice_extremo]):
                indice_extremo = j
        # Intercambia el elemento mínimo o máximo con el primer elemento no ordenado
        lista[i], lista[indice_extremo] = lista[indice_extremo], lista[i]
    return lista

# Insertion Sort
def insertion_sort(lista, ascendente=True):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mueve los elementos de la lista que son mayores (o menores) que la clave
        while j >= 0 and ((ascendente and lista[j] > clave) or (not ascendente and lista[j] < clave)):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]

print("Lista original:", lista)

# Ordenar usando Bubble Sort (ascendente)
print("Bubble Sort Ascendente:", bubble_sort(lista.copy(), True))

# Ordenar usando Bubble Sort (descendente)
print("Bubble Sort Descendente:", bubble_sort(lista.copy(), False))

# Ordenar usando Selection Sort (ascendente)
print("Selection Sort Ascendente:", selection_sort(lista.copy(), True))

# Ordenar usando Selection Sort (descendente)
print("Selection Sort Descendente:", selection_sort(lista.copy(), False))

# Ordenar usando Insertion Sort (ascendente)
print("Insertion Sort Ascendente:", insertion_sort(lista.copy(), True))

# Ordenar usando Insertion Sort (descendente)
print("Insertion Sort Descendente:", insertion_sort(lista.copy(), False))

    

## Ejercicio -10 [Aura Pico] cc: 1097498480 👨‍🦯