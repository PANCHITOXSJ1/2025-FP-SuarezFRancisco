# ------------------------------------------------------------
# TAREA: Lectura y Escritura de Archivos de Texto en Python
# Autor: [Tu Nombre]
# Archivo: my_notes.py
# Descripción:
#   Este programa crea un archivo de texto, escribe notas personales,
#   las lee línea por línea y las muestra en pantalla.
# ------------------------------------------------------------

# Escritura de Archivo de Texto
# Se crea (o sobrescribe) un archivo llamado 'my_notes.txt'
with open("my_notes.txt", "w") as archivo:
    # write() se usa para escribir texto en el archivo
    archivo.write("1. Hoy aprendí a manipular archivos en Python.\n")
    archivo.write("2. La práctica es importante para mejorar mis habilidades.\n")
    archivo.write("3. Cerrar correctamente los archivos evita errores, Francisco Suarez.\n")

# Lectura de Archivo de Texto
# Ahora abrimos el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as archivo:
    print("Contenido del archivo my_notes.txt:\n")
    # readline() lee una línea por vez
    linea = archivo.readline()
    while linea:
        print(linea.strip())  # .strip() elimina saltos de línea al imprimir
        linea = archivo.readline()

# Nota: no es necesario usar archivo.close() porque 'with' lo cierra automáticamente
