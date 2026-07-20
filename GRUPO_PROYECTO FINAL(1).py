# ==========================================
# PROYECTO FINAL: POLIRESCUE TECHNOLOGIES
# Algoritmos y Estructuras de Datos
# ==========================================
# ==========================
# LISTAS DEL SISTEMA
# ==========================
drones = []
misiones = []
zonas = []
rutas = []
# ==========================
# FUNCIONES DE VALIDACIÓN
# ==========================
def leer_entero(mensaje):
    """Evita que el programa se caiga si no se ingresa un número entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido.")
def leer_flotante(mensaje):
    """Evita que el programa se caiga si no se ingresa un número decimal."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número decimal válido.")
# ==========================
# DATOS DE PRUEBA
# ==========================
drones.append({
    "codigo": "D001", "modelo": "DJI Mini 3", "velocidad": 60, 
    "capacidad": 5, "bateria": 90, "estado": "Disponible"
})
drones.append({
    "codigo": "D002", "modelo": "DJI Mavic Air", "velocidad": 75, 
    "capacidad": 8, "bateria": 80, "estado": "Disponible"
})
misiones.append({
    "codigo": "M001", "zona": "Zona Norte", "tipo_emergencia": "Incendio", 
    "prioridad": 8, "personas_afectadas": 15, "distancia": 12.0, "estado": "Pendiente"
})
misiones.append({
    "codigo": "M002", "zona": "Zona Sur", "tipo_emergencia": "Inundación", 
    "prioridad": 5, "personas_afectadas": 8, "distancia": 20.0, "estado": "Pendiente"
})
zonas.append({"nombre": "Base", "descripcion": "Centro de operaciones"})
zonas.append({"nombre": "Hospital", "descripcion": "Hospital General"})
zonas.append({"nombre": "Zona Norte", "descripcion": "Sector afectado"})

rutas.append({"codigo": "R001", "origen": "Base", "destino": "Hospital", "distancia": 4.0})
rutas.append({"codigo": "R002", "origen": "Hospital", "destino": "Zona Norte", "distancia": 6.0})
# ==========================
# FUNCIONES DRONES
# ==========================
def registrar_dron():
    print("\n========== REGISTRAR DRON ==========")
    
    # MEJORA: Validar código no vacío
    while True:
        codigo = input("Código: ").strip()
        if codigo != "":
            break
        print("El código no puede estar vacío.")

    for dron in drones:
        if dron["codigo"] == codigo:
            print("Ese código ya existe.")
            return

    modelo = input("Modelo: ")
    velocidad = leer_entero("Velocidad (km/h): ")
    capacidad = leer_entero("Capacidad (kg): ")
    
    # MEJORA: Validar rango de batería
    while True:
        bateria = leer_entero("Nivel de batería (%): ")
        if 0 <= bateria <= 100:
            break
        print("Error: la batería debe estar entre 0 y 100.")

    estado = input("Estado (Disponible/Ocupado): ").strip()

    drones.append({
        "codigo": codigo, "modelo": modelo, "velocidad": velocidad,
        "capacidad": capacidad, "bateria": bateria, "estado": estado
    })
    print("\nDron registrado correctamente.")

def mostrar_drones():
    print("\n========== DRONES LISTADOS ==========")
    if not drones:
        print("No existen drones registrados.")
        return
    for i, dron in enumerate(drones, 1):
        print(f"\n[Dron {i}] -> Código: {dron['codigo']} | Modelo: {dron['modelo']} | Velocidad: {dron['velocidad']} km/h | Capacidad: {dron['capacidad']} kg | Batería: {dron['bateria']}% | Estado: {dron['estado']}")

def eliminar_dron():
    print("\n========== ELIMINAR DRON ==========")
    if not drones:
        print("No existen drones registrados.")
        return
    codigo = input("Ingrese el código del dron: ").strip()
    for dron in drones:
        if dron["codigo"] == codigo:
            drones.remove(dron)
            print("Dron eliminado correctamente.")
            return
    print("❌ No existe ese dron.")

def menu_drones():
    while True:
        print("\n==============================")
        print("      GESTIÓN DRONES")
        print("==============================")
        print("1. Registrar Dron")
        print("2. Mostrar Drones")
        print("3. Eliminar Dron")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1": registrar_dron()
        elif opcion == "2": mostrar_drones()
        elif opcion == "3": eliminar_dron()
        elif opcion == "4": break
        else: print("Opción incorrecta.")


# ==========================
# FUNCIONES MISIONES
# ==========================
def registrar_mision():
    print("\n========== REGISTRAR MISIÓN ==========")
    
    # MEJORA: Validar código no vacío
    while True:
        codigo = input("Código: ").strip()
        if codigo != "":
            break
        print("El código no puede estar vacío.")

    for mision in misiones:
        if mision["codigo"] == codigo:
            print("Ese código ya existe.")
            return

    zona = input("Zona de la emergencia: ")
    tipo = input("Tipo de emergencia (Terremoto/Incendio/Inundación/Deslizamiento): ")
    prioridad = leer_entero("Prioridad (1-10): ")
    personas = leer_entero("Personas afectadas: ")
    distancia = leer_flotante("Distancia (km): ")
    estado = input("Estado (Pendiente/Atendida): ").strip()

    misiones.append({
        "codigo": codigo, "zona": zona, "tipo_emergencia": tipo,
        "prioridad": prioridad, "personas_afectadas": personas, 
        "distancia": distancia, "estado": estado
    })
    print("\nMisión registrada correctamente.")

def mostrar_misiones():
    print("\n========== MISIONES LISTADAS ==========")
    if not misiones:
        print("No existen misiones registradas.")
        return
    for i, m in enumerate(misiones, 1):
        print(f"\n[Misión {i}] -> Código: {m['codigo']} | Zona: {m['zona']} | Emergencia: {m['tipo_emergencia']} | Prioridad: {m['prioridad']} | Personas Afectadas: {m['personas_afectadas']} | Distancia: {m['distancia']} km | Estado: {m['estado']}")
def eliminar_mision():
    print("\n========== ELIMINAR MISIÓN ==========")
    if not misiones:
        print("No existen misiones registradas.")
        return
    codigo = input("Ingrese el código de la misión: ").strip()
    for m in misiones:
        if m["codigo"] == codigo:
            misiones.remove(m)
            print("Misión eliminada correctamente.")
            return
    print("❌ No existe esa misión.")
def menu_misiones():
    while True:
        print("\n==============================")
        print("     GESTIÓN MISIONES")
        print("==============================")
        print("1. Registrar Misión")
        print("2. Mostrar Misiones")
        print("3. Eliminar Misión")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1": registrar_mision()
        elif opcion == "2": mostrar_misiones()
        elif opcion == "3": eliminar_mision()
        elif opcion == "4": break
        else: print("Opción incorrecta.")
# ==========================
# FUNCIONES ZONAS
# ==========================
def registrar_zona():
    print("\n========== REGISTRAR ZONA ==========")
    nombre = input("Nombre de la zona: ").strip()
    for z in zonas:
        if z["nombre"].lower() == nombre.lower():
            print("Esa zona ya existe.")
            return
    descripcion = input("Descripción: ")
    zonas.append({"nombre": nombre, "descripcion": descripcion})
    print("\nZona registrada correctamente.")
def mostrar_zonas():
    print("\n========== ZONAS LISTADAS ==========")
    if not zonas:
        print("No existen zonas registradas.")
        return
    for i, z in enumerate(zonas, 1):
        print(f"   {i}. Nombre: {z['nombre']} | Descripción: {z['descripcion']}")
def eliminar_zona():
    print("\n========== ELIMINAR ZONA ==========")
    if not zonas:
        print("No existen zonas registradas.")
        return
    nombre = input("Ingrese el nombre de la zona a eliminar: ").strip()
    for z in zonas:
        if z["nombre"].lower() == nombre.lower():
            zonas.remove(z)
            print("Zona eliminada correctamente.")
            return
    print("No existe esa zona.")
def menu_zonas():
    while True:
        print("\n==============================")
        print("      GESTIÓN ZONAS")
        print("==============================")
        print("1. Registrar Zona")
        print("2. Mostrar Zonas")
        print("3. Eliminar Zona")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1": registrar_zona()
        elif opcion == "2": mostrar_zonas()
        elif opcion == "3": eliminar_zona()
        elif opcion == "4": break
        else: print(" Opción incorrecta.")
# ==========================
# FUNCIONES RUTAS
# ==========================
def registrar_ruta():
    print("\n========== REGISTRAR RUTA ==========")
    codigo = input("Código de Ruta: ").strip()
    for r in rutas:
        if r["codigo"] == codigo:
            print(" Ese código de ruta ya existe.")
            return
    origen = input("Zona Origen: ").strip()
    destino = input("Zona Destino: ").strip()
    distancia = leer_flotante("Distancia de la ruta (km): ")
    rutas.append({
        "codigo": codigo, "origen": origen, "destino": destino, "distancia": distancia
    })
    print("\n Ruta registrada correctamente.")
def mostrar_rutas():
    print("\n========== RUTAS LISTADAS ==========")
    if not rutas:
        print("No existen rutas registradas.")
        return
    for i, r in enumerate(rutas, 1):
        print(f"   {i}. Código: {r['codigo']} | Conexión: {r['origen']} ---> {r['destino']} | Distancia: {r['distancia']} km")
def eliminar_ruta():
    print("\n========== ELIMINAR RUTA ==========")
    if not rutas:
        print("No existen rutas registradas.")
        return
    codigo = input("Ingrese el código de la ruta: ").strip()
    for r in rutas:
        if r["codigo"] == codigo:
            rutas.remove(r)
            print(" Ruta eliminada correctamente.")
            return
    print(" No existe esa ruta.")
def menu_rutas():
    while True:
        print("\n==============================")
        print("      GESTIÓN RUTAS")
        print("==============================")
        print("1. Registrar Ruta")
        print("2. Mostrar Rutas")
        print("3. Eliminar Ruta")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1": registrar_ruta()
        elif opcion == "2": mostrar_rutas()
        elif opcion == "3": eliminar_ruta()
        elif opcion == "4": break
        else: print(" Opción incorrecta.")
#PARTE 2 - NOA
# ==================================================
# ORGANIZACIÓN DE MISIONES
# ==================================================
def mostrar_prioridades():
    print("\nMISIÓN\tPRIORIDAD")
    for m in misiones:
        print(m["codigo"], "\t", m["prioridad"])
def mostrar_baterias():
    print("\nDRON\tBATERÍA")
    for d in drones:
        print(d["codigo"], "\t", str(d["bateria"])+"%")
# ==================================================
# BUBBLE SORT
# Ordenar misiones por prioridad (Mayor a menor)
# ==================================================
def bubble_sort_prioridad():
    if len(misiones) == 0:
        print("No existen misiones.")
        return
    n = len(misiones)
    print("\n=========== BUBBLE SORT ===========")
    for i in range(n-1):
        for j in range(n-1-i):
            print("\nComparando...")
            print(misiones[j]["codigo"], "(", misiones[j]["prioridad"], ")",
                  "con",
                  misiones[j+1]["codigo"], "(", misiones[j+1]["prioridad"], ")")
            if misiones[j]["prioridad"] < misiones[j+1]["prioridad"]:
                print("Intercambiando...")
                aux = misiones[j]
                misiones[j] = misiones[j+1]
                misiones[j+1] = aux
            print("Lista actual...")
            for x in misiones:
                print(x["codigo"], "-", x["prioridad"])
    print("\nMISIÓNES ORDENADAS")
    mostrar_prioridades()
# ==================================================
# INSERTION SORT
# Ordenar drones por batería (Mayor a menor)
# =================================================
def insertion_sort_bateria():
    if len(drones) == 0:
        print("No existen drones.")
        return
    print("\n=========== INSERTION SORT ===========")
    for i in range(1, len(drones)):
        actual = drones[i]
        print("\nInsertando...")
        print(actual["codigo"], "-", actual["bateria"], "%")
        j = i - 1
        while j >= 0 and drones[j]["bateria"] < actual["bateria"]:
            print("Moviendo...")
            print(drones[j]["codigo"])
            drones[j+1] = drones[j]
            print("Lista actual...")
            for d in drones:
                print(d["codigo"], "-", d["bateria"], "%")
            j = j - 1
        drones[j+1] = actual
    print("\nDRONES ORDENADOS")
    mostrar_baterias()
# ==================================================
# MERGE SORT
# Ordenar drones por velocidad (Mayor a menor)
# ==================================================
def merge(lista, izquierda, mitad, derecha):
    n1 = mitad - izquierda + 1
    n2 = derecha - mitad
    L = []
    R = []
    i = 0
    while i < n1:
        L.append(lista[izquierda + i])
        i += 1
    j = 0
    while j < n2:
        R.append(lista[mitad + 1 + j])
        j += 1
    print("\nMezclando...")
    i = 0
    j = 0
    k = izquierda
    while i < n1 and j < n2:
        if L[i]["velocidad"] >= R[j]["velocidad"]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        lista[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        lista[k] = R[j]
        j += 1
        k += 1
    print("Resultado parcial:")
    x = izquierda
    while x <= derecha:
        print(lista[x]["codigo"], "-", lista[x]["velocidad"], "km/h")
        x += 1
def merge_sort(lista, izquierda, derecha):
    if izquierda < derecha:
        mitad = (izquierda + derecha) // 2
        print("\nDividiendo...")
        print("Inicio:", izquierda,
              "Mitad:", mitad,
              "Fin:", derecha)
        merge_sort(lista, izquierda, mitad)
        merge_sort(lista, mitad + 1, derecha)
        merge(lista, izquierda, mitad, derecha)
def ejecutar_merge_sort():
    if len(drones) == 0:
        print("No existen drones.")
        return
    print("\n=========== MERGE SORT ===========")
    merge_sort(drones, 0, len(drones)-1)
    print("\nDRONES ORDENADOS POR VELOCIDAD")
    for d in drones:
        print(
            d["codigo"],
            "-",
            d["velocidad"],
            "km/h"
        )
# ==================================================
# QUICK SORT
# Ordenar misiones por distancia (Menor a mayor)
# ==================================================
def particion(lista, inicio, fin):
    pivote = lista[fin]
    print("\nPivote:")
    print(pivote["codigo"], "-", pivote["distancia"], "km")
    i = inicio - 1
    for j in range(inicio, fin):
        print("Comparando", lista[j]["codigo"], "con el pivote")
        if lista[j]["distancia"] <= pivote["distancia"]:
            i += 1
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            print("Partición:")
            for x in lista:
                print(x["codigo"], "-", x["distancia"], "km")
    aux = lista[i + 1]
    lista[i + 1] = lista[fin]
    lista[fin] = aux
    print("\nResultado:")
    for x in lista:
        print(x["codigo"], "-", x["distancia"], "km")
    return i + 1
def quick_sort(lista, inicio, fin):
    if inicio < fin:
        pi = particion(lista, inicio, fin)
        quick_sort(lista, inicio, pi - 1)
        quick_sort(lista, pi + 1, fin)
def ejecutar_quick_sort():
    if len(misiones) == 0:
        print("No existen misiones.")
        return
    print("\n=========== QUICK SORT ===========")
    quick_sort(misiones, 0, len(misiones)-1)
    print("\nMISIONES ORDENADAS POR DISTANCIA")
    for m in misiones:
        print(
            m["codigo"],
            "-",
            m["distancia"],
            "km"
        )
# ==================================================
# MENÚ ORGANIZACIÓN DE MISIONES
# ==================================================
def menu_organizacion():
    while True:
        print("\n===================================")
        print("   ORGANIZACIÓN DE MISIONES")
        print("===================================")
        print("1. Bubble Sort (Prioridad)")
        print("2. Insertion Sort (Batería)")
        print("3. Merge Sort (Velocidad)")
        print("4. Quick Sort (Distancia)")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            bubble_sort_prioridad()
        elif opcion == "2":
            insertion_sort_bateria()
        elif opcion == "3":
            ejecutar_merge_sort()
        elif opcion == "4":
            ejecutar_quick_sort()
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta.")
#Parte 3- Tati
# ==================================
# Busqueda lineal de dron por bateria
# ==================================
def buscar_lineal_por_bateria():
    print("\n========== DRON POR BATERÍA ==========")
    if not drones:
        print("No hay drones registrados en el sistema.")
        return
    bateria_buscar = leer_entero("Ingrese el nivel de batería (%) que desea buscar: ")
    print(f"\n[Buscando en Drones con {bateria_buscar}% de batería]")
    comp_drones = 0
    encontrado_dron = False
    
    for dron in drones:
        comp_drones += 1
        print(f"   -> Elemento comparado: Código: {dron['codigo']} \nBatería: {dron['bateria']}%")
        if dron["bateria"] == bateria_buscar:
            print(f"   ¡Éxito! Dron encontrado: {dron['modelo']} - {dron['estado']}")
            encontrado_dron = True
            break
    print(f"   Comparaciones realizadas en Drones: {comp_drones}")
    if not encontrado_dron:
        print("   No se encontró ningún dron con esa batería.")
# ==================================
# Busqueda lineal de dron por prioridad
# ==================================
def buscar_lineal_mision_prioridad():
    print("\n========== MISIÓN POR PRIORIDAD ==========")
    if not misiones:
        print("No hay misiones registradas en el sistema.")
        return
    prioridad_buscar = leer_entero("Ingrese la prioridad (1-10) de la misión a buscar: ")
    comparaciones = 0
    encontrado = False
    for m in misiones:
        comparaciones += 1
        print(f"   -> Elemento comparado: Misión Código: {m['codigo']} | Prioridad: {m['prioridad']}")
        if m["prioridad"] == prioridad_buscar:
            print(f"\n   ¡Éxito! Misión encontrada en: {m['zona']} | Emergencia: {m['tipo_emergencia']}")
            encontrado = True
            break
    print(f"   Comparaciones realizadas en Misiones: {comparaciones}")
    if not encontrado:
        print("   No se encontró ninguna misión con ese nivel de prioridad.")

# ==================================
# Busqueda binaria de dron por codigo
# ==================================
def busqueda_binaria_dron_codigo():
    print("\n========== BÚSQUEDA DRON POR CÓDIGO ==========")
    if not drones:
        print("No hay drones registrados para buscar.")
        return
    codigo_buscar = input("Ingrese el código del dron a buscar (ej: D001): ").strip()
    #ORDENAMIENTO MANUAL    
    drones_ordenados = []
    for d in drones:
        drones_ordenados.append(d)
    n = len(drones_ordenados)
    for i in range(n):
        for j in range(n - 1):
            if drones_ordenados[j]["codigo"] > drones_ordenados[j + 1]["codigo"]:
                aux = drones_ordenados[j]
                drones_ordenados[j] = drones_ordenados[j + 1]
                drones_ordenados[j + 1] = aux
    #BUSQUEDA   
    low = 0
    high = len(drones_ordenados) - 1
    encontrado = False
    while low <= high:
        mid = (low + high) // 2
        valor_medio = drones_ordenados[mid]["codigo"]
        print(f"   low: {low} | high: {high} | mid: {mid} | valor medio (código): {valor_medio}")
        if valor_medio == codigo_buscar:
            print(f"\n   ¡Éxito! Dron encontrado.")
            print(f"   Modelo: {drones_ordenados[mid]['modelo']} \n Batería: {drones_ordenados[mid]['bateria']}% | Estado: {drones_ordenados[mid]['estado']}")
            encontrado = True
            break
        elif valor_medio < codigo_buscar:
            low = mid + 1  
        else:
            high = mid - 1 
    if not encontrado:
        print(f"   No se encontró ningún dron con el código '{codigo_buscar}'.")
def menu_busquedas():
    while True:
        print("\n==============================")
        print(" ALGORITMOS DE BÚSQUEDA")
        print("==============================")
        print("1. Buscar Dron por Batería (Lineal)")
        print("1. Buscar Mision por Batería (Lineal)")
        print("2. Buscar Dron por Código (Binaria)")
        print("3. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar_lineal_por_bateria()
        elif opcion == "2":
            buscar_lineal_mision_bateria()
        elif opcion == "3":
            busqueda_binaria_dron_codigo()
        elif opcion == "4":
            break
        else:
            print("Opción incorrecta.")
# =====================================================================
# 4. COLA DE MISIONES PENDIENTES
# =====================================================================
cola_fifo_misiones = [m for m in misiones if m["estado"] == "Pendiente"]
def actualizar_cola_desde_sistema():
    """Sincroniza la cola si registraste misiones nuevas en el menú de misiones"""
    cola_fifo_misiones.clear()
    for m in misiones:
        if m["estado"] == "Pendiente":
            cola_fifo_misiones.append(m)
def agregar_mision_a_cola():
    print("\n========== AGREGAR MISIÓN A COLA FIFO ==========")
    registrar_mision()
    actualizar_cola_desde_sistema()
def atender_mision_cola():
    print("\n========== ATENDER MISIÓN ==========")
    actualizar_cola_desde_sistema()
    if len(cola_fifo_misiones) == 0:
        print("No hay misiones pendientes en la cola FIFO.")
        return 
    mision_atendida = cola_fifo_misiones.pop(0)
    mision_atendida["estado"] = "Atendida"
    for m in misiones:
        if m["codigo"] == mision_atendida["codigo"]:
            m["estado"] = "Atendida"        
    print(f"Misión [Código: {mision_atendida['codigo']}] en {mision_atendida['zona']} ha sido ATENDIDA.")
    print("Salió de la cola de espera y su estado cambió a 'Atendida'.")

def mostrar_siguiente_mision_cola():
    print("\n========== SIGUIENTE MISIÓN EN COLA ==========")
    actualizar_cola_desde_sistema()
    if len(cola_fifo_misiones) == 0:
        print("La cola está vacía. No hay próximas misiones pendientes.")
    else:
        siguiente = cola_fifo_misiones[0]
        print(f"Próxima misión a atender:")
        print(f"-> Código: {siguiente['codigo']} \n Zona: {siguiente['zona']} \n Emergencia: {siguiente['tipo_emergencia']} \n Prioridad: {siguiente['prioridad']}")

def menu_cola_misiones():
    while True:
        print("\n==============================")
        print(" COLA DE MISIONES FIFO")
        print("==============================")
        print("1. Agregar Misión")
        print("2. Atender Misión (FIFO)")
        print("3. Mostrar Siguiente Misión")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_mision_a_cola()
        elif opcion == "2":
            atender_mision_cola()
        elif opcion == "3":
            mostrar_siguiente_mision_cola()
        elif opcion == "4":
            break
        else:
            print("Opción incorrecta.")
# ==========================
# MENÚ PRINCIPAL
# ==========================
def menu_principal():
    while True:
        print("\n==========================================")
        print("   SISTEMA POLIRESCUE TECHNOLOGIES")
        print("==========================================")
        print("1. Gestionar Drones")
        print("2. Gestionar Misiones")
        print("3. Gestionar Zonas")
        print("4. Gestionar Rutas")
        print("5. Organización de misiones")
        print("6. Busqueda de dron")
        print("7. Gestionar misiones pendientes")
        print("8. Simulación de Rescate")
        print("9. Salir")
        
        opcion = input("Seleccione una opción general: ")
        
        if opcion == "1": menu_drones()
        elif opcion == "2": menu_misiones()
        elif opcion == "3": menu_zonas()
        elif opcion == "4": menu_rutas()
        elif opcion == "5": menu_organizacion()
        elif opcion == "6": menu_busquedas()
        elif opcion == "7": menu_cola_misiones()
        elif opcion == "8": 
            print("\n Esta sección ejecutará el flujo de simulación completo de tus compañeros (Pasos 1-9).")
        elif opcion == "9":
            print("\n Saliendo del sistema de rescate. ¡Buen trabajo!")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")
# ==========================
# GRAFO DE ZONAS
# ==========================
grafo = {}
def construir_grafo():
    """
    Construye el grafo utilizando las rutas registradas.
    Cada zona es un nodo y cada ruta una arista.
    """
    global grafo
    grafo = {}
    for ruta in rutas:
        origen = ruta["origen"]
        destino = ruta["destino"]
        distancia = ruta["distancia"]
        if origen not in grafo:
            grafo[origen] = []
        if destino not in grafo:
            grafo[destino] = []
        # Grafo no dirigido
        grafo[origen].append((destino, distancia))
        grafo[destino].append((origen, distancia))
# ==================================================
# BFS (Breadth First Search)
# Verificar si existe una ruta entre dos zonas
# ================================================= 
from collections import deque
def bfs(origen, destino):
    construir_grafo()
    if origen not in grafo:
        print("La zona de origen no existe.")
        return False
    if destino not in grafo:
        print("La zona de destino no existe.")
        return False
    cola = deque()
    visitados = []
    cola.append(origen)
    visitados.append(origen)
    print("\n=========== BFS ===========")
    while cola:
        actual = cola.popleft()
        print("\nVisitando:", actual)
        print("Cola actual:")
        if len(cola) == 0:
            print("Vacía")
        else:
            for nodo in cola:
                print("->", nodo)
        print("Nodos visitados:")
        for nodo in visitados:
            print("->", nodo)
        if actual == destino:
            print("\nCamino encontrado.")
            return True
        for vecino, distancia in grafo[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)
    print("\nNo existe un camino entre", origen, "y", destino)
    return False
# ==================================================
# DIJKSTRA
# Ruta mínima entre dos zonas
# ==================================================
import math
def dijkstra(origen, destino):
    construir_grafo()
    if origen not in grafo:
        print("La zona de origen no existe.")
        return
    if destino not in grafo:
        print("La zona de destino no existe.")
        return
    # Inicializar distancias
    distancias = {}
    anteriores = {}
    visitados = []
    for nodo in grafo:
        distancias[nodo] = math.inf
        anteriores[nodo] = None
    distancias[origen] = 0
    while len(visitados) < len(grafo):
        # Buscar el nodo con menor distancia
        actual = None
        menor = math.inf
        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < menor:
                menor = distancias[nodo]
                actual = nodo
        if actual is None:
            break
        print("\n================================")
        print("Nodo actual:", actual)
        visitados.append(actual)
        # Actualizar vecinos
        for vecino, peso in grafo[actual]:
            if vecino not in visitados:
                nueva = distancias[actual] + peso
                if nueva < distancias[vecino]:
                    distancias[vecino] = nueva
                    anteriores[vecino] = actual
        print("\nDistancias:")
        for nodo in distancias:
            if distancias[nodo] == math.inf:
                print(nodo, "= Infinito")
            else:
                print(nodo, "=", distancias[nodo], "km")
        print("\nRuta parcial:")
        for nodo in anteriores:
            if anteriores[nodo] is not None:
                print(anteriores[nodo], "->", nodo)
    # Verificar si existe ruta
    if distancias[destino] == math.inf:
        print("\nNo existe una ruta.")
        return
    # Reconstrucción de la ruta
    ruta = []
    actual = destino
    while actual is not None:
        ruta.insert(0, actual)
        actual = anteriores[actual]
    print("\n================================")
    print("RUTA MÍNIMA")

    for i in range(len(ruta)):
        print(ruta[i], end="")
        if i != len(ruta)-1:
            print(" -> ", end="")
    print("\n")
    print("Distancia total:", distancias[destino], "km")
    # Ejecución inicial del programa
if __name__ == "__main__":
    menu_principal()
