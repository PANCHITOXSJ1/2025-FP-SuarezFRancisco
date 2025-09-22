# Definir función para calcular descuento con valor por defecto
def calcular_descuento(monto_total, porcentaje_descuento=15):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
monto = float(input("Ingrese el monto total de la compra: "))
descuento = calcular_descuento(monto)
total_a_pagar = monto - descuento

print("\n--- Resultado ---")
print(f"Monto total: {monto}")
print(f"Descuento aplicado ({15}%): {descuento}")
print(f"Total a pagar después del descuento: {total_a_pagar}")
