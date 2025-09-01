# Programa 1: Búsqueda en una matriz bidimensional (3x3)

# Definimos la matriz 3x3
matriz = [
    [10, 25, 30],
    [45, 50, 65],
    [70, 85, 90]
]

# Función de búsqueda en matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # filas
        for j in range(len(matriz[i])):   # columnas
            if matriz[i][j] == valor:
                return (i, j)  # retorna posición (fila, columna)
    return None

# Valor a buscar
valor_buscar = 8

resultado = buscar_valor(matriz, valor_buscar)

# Mostrar resultados
print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor {valor_buscar} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\n❌ El valor {valor_buscar} NO se encontró en la matriz.")
