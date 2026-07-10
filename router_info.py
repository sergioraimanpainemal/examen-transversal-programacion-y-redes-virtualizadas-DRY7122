# ==========================================
# ÍTEM 7: INTERACCIÓN CSR1000v CON NETMIKO
# ==========================================
from netmiko import ConnectHandler

router_csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.128',
    'username': 'cisco',
    'password': 'cisco123!',
    'secret': 'cisco',
}

comandos_config_eigrp = [
    'router eigrp 100',
    'address-family ipv4 unicast autonomous-system 100',
    'network 192.168.100.0 0.0.0.255',
    'exit-address-family',
    'address-family ipv6 unicast autonomous-system 100',
    'exit-address-family'
]

try:
    print("Conectando al router ETW-CSR1000v via SSH...")
    net_connect = ConnectHandler(**router_csr)
    net_connect.enable()
    
    print("Configurando EIGRP Nombrado...")
    net_connect.send_config_set(comandos_config_eigrp)
    net_connect.send_command("write memory")

    # 1. Obtener verificación de EIGRP (Cambiado a 'eigrp' para que muestre datos reales)
    print("Obteniendo verificación de EIGRP...")
    show_eigrp = net_connect.send_command("show running-config | section eigrp")

    # 2. Obtener estado de las interfaces e IPs
    print("Obteniendo estado de interfaces...")
    show_interfaces = net_connect.send_command("show ip interface brief")

    # 3. Obtener todo el running-config
    print("Obteniendo running-config completo...")
    show_run = net_connect.send_command("show running-config")

    # 4. Obtener el show version
    print("Obteniendo versión del sistema...")
    show_version = net_connect.send_command("show version")

    net_connect.disconnect()

    # ==================================================
    # MOSTRAR ABSOLUTAMENTE TODO EN LA TERMINAL
    # ==================================================
    print("\n" + "="*60)
    print("          TODOS LOS RESULTADOS DEL ROUTER (ÍTEM 7)        ")
    print("="*60)
    
    print("\n==========================================")
    print("1. CONFIGURACIÓN EIGRP NOMBRADO")
    print("==========================================")
    print(show_eigrp if show_eigrp.strip() else "No se encontró configuración de EIGRP.")
    
    print("\n==========================================")
    print("2. ESTADO DE INTERFACES E IPs")
    print("==========================================")
    print(show_interfaces)
    
    print("\n==========================================")
    print("3. SHOW VERSION")
    print("==========================================")
    print(show_version)

    print("\n==========================================")
    print("4. RUNNING-CONFIG (PRIMERAS LÍNEAS)")
    print("==========================================")
    # Mostramos las primeras 30 líneas en la terminal para no colapsar la pantalla, 
    # pero el archivo .txt tendrá el archivo completo.
    lineas_run = show_run.splitlines()
    print("\n".join(lineas_run[:30]))
    print("\n... [Configuración completa guardada en resultado_running_config.txt] ...")

    # Guardar respaldos en archivos de texto
    with open("resultado_eigrp.txt", "w") as f: f.write(show_eigrp)
    with open("resultado_interfaces.txt", "w") as f: f.write(show_interfaces)
    with open("resultado_running_config.txt", "w") as f: f.write(show_run)
    with open("resultado_version.txt", "w") as f: f.write(show_version)

    print("\n[✔] ¡Proceso completado! Todo se imprimió en pantalla y se guardó en los .txt.")

except Exception as e:
    print(f"\n[!] Error: {e}")
