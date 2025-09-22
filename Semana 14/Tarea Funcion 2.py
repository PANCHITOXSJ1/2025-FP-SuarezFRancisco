# Definir función para calcular descuento
def calcular_descuento(monto_total, porcentaje_descuento):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
monto = float(input("Ingrese el monto total de la compra: "))
porcentaje = float(input("Ingrese el porcentaje de descuento a aplicar: "))

descuento = calcular_descuento(monto, porcentaje)
total_a_pagar = monto - descuento

print("\n--- Resultado ---")
print(f"Monto total: {monto}")
print(f"Descuento aplicado ({porcentaje}%): {descuento}")
print(f"Total a pagar después del descuento: {total_a_pagar}")
