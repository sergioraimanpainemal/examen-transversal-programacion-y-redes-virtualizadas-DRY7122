print("========================================")
print("   Asistente de Validación de VLANs     ")
print("========================================")

try:

    vlan = int(input("Por favor, ingrese el número de VLAN a evaluar: "))

 
    if 1 <= vlan <= 1005:
        print(f"\n[RESULTADO]: La VLAN {vlan} pertenece al Rango Normal.")
        print("-> Nota: Las VLANs 1 y 1002-1005 se crean automáticamente y no se pueden eliminar.")

    elif 1006 <= vlan <= 4094:
        print(f"\n[RESULTADO]: La VLAN {vlan} pertenece al Rango Extendido.")
        print("-> Nota: Utilizadas comúnmente en grandes corporaciones o proveedores de servicios.")

    else:
        print(f"\n[ERROR]: El número {vlan} está fuera del rango permitido global (1 - 4094).")

except ValueError:
    print("\n[ERROR]: Entrada no válida. Por favor, digite un número entero.")
