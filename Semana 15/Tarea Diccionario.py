# Diccionario con información personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": ["Quito"],       # Usamos lista para permitir múltiples ciudades
    "profesion": ["Estudiante"] # Usamos lista para permitir múltiples profesiones
}

# Imprimir el diccionario original
print("Diccionario Original:\n")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
print("\n" + "="*40 + "\n")  # Línea de separación

# --- Modificaciones ---
# Cambiar ciudad agregando otra
informacion_personal["ciudad"].append("Guayaquil")

# Agregar nueva profesión
informacion_personal["profesion"].append("Ingeniero")

# Verificar existencia de clave 'telefono'
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = ["0991234567"]

# Eliminar la clave 'edad'
del informacion_personal["edad"]

# Imprimir el diccionario modificado
print("Diccionario Modificado:\n")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
