# Programa 2: Ordenación de todas las filas en una matriz bidimensional (3x3)

# Definimos la matriz 3x3
matriz = [
    [30, 10, 20],
    [60, 50, 40],
    [90, 80, 70]
]

# Implementación de Bubble Sort para ordenar una fila
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar todas las filas de la matriz
for i in range(len(matriz)):
    matriz[i] = bubble_sort(matriz[i])

print("\nMatriz con todas las filas ordenadas:")
for fila in matriz:
    print(fila)
