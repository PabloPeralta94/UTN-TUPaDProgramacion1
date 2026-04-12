# ============================================================
#  PROGRAMACIÓN 1 Pablo Peralta
#  TP Integrador: Repetitivas, Condicionales y Secuenciales
# ============================================================


# ============================================================
# Ejercicio 1 - "Caja del Kiosco"
# Objetivo: Simular una compra con validaciones y cálculo de total.
# Requisitos:
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#    .isdigit() en while).
# 3. Por cada producto (usar for):
#    - Pedir precio (entero, validar .isdigit()).
#    - Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#      cualquier mayuscula/minuscula).
#    - Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:
#    - Total sin descuentos
#    - Total con descuentos
#    - Ahorro total
#    - Promedio por producto (usar float y formatear con :.2f)
# Validaciones obligatorias:
# - Sin try/except.
# - No aceptar vacío en nombre (si queda vacío, es error).
# - Cantidad > 0 (si ingresa 0, volver a pedir).
# ============================================================

nombre_cliente = input("Ingrese su nombre: ")
while not nombre_cliente.isalpha():
    print("Error: el nombre solo puede contener letras y no puede estar vacío.")
    nombre_cliente = input("Ingrese su nombre: ")

cantidad_str = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad_str = input("Ingrese la cantidad de productos a comprar: ")
cantidad_productos = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad_productos + 1):
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: ingrese un número entero válido.")
        precio_str = input(f"Producto {i} - Precio: ")
    precio = int(precio_str)

    descuento_str = input(f"Producto {i} - Descuento (S/N): ")
    while descuento_str.lower() not in ["s", "n"]:
        print("Error: ingrese S o N.")
        descuento_str = input(f"Producto {i} - Descuento (S/N): ")

    total_sin_descuento += precio

    if descuento_str.lower() == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"\nCliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# ============================================================
# Ejercicio 2 - "Acceso al Campus y Menú Seguro"
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos:
# 1. Definir credenciales fijas en el código:
#    - usuario correcto: "alumno"
#    - clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar "Cuenta bloqueada" y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#    1. Ver estado de inscripción (mostrar "Inscripto")
#    2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#    3. Mostrar mensaje motivacional (1 frase)
#    4. Salir
# 5. Validación del menú:
#    - Debe ser número (.isdigit())
#    - Debe estar entre 1 y 4
# Cambio de clave:
# - La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.
# ============================================================

USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

intentos = 0
acceso = False

while intentos < 3:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")

    if usuario_ingresado == USUARIO_CORRECTO and clave_ingresada == CLAVE_CORRECTA:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    clave_actual = CLAVE_CORRECTA
    en_menu = True

    while en_menu:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            print("Estado de inscripción: Inscripto.")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirmacion = input("Confirmar nueva clave: ")
            if nueva_clave == confirmacion:
                clave_actual = nueva_clave
                print("Clave actualizada correctamente.")
            else:
                print("Error: las claves no coinciden. No se realizó el cambio.")

        elif opcion == 3:
            print("¡El esfuerzo de hoy es el éxito de mañana. Seguí adelante!")

        elif opcion == 4:
            print("Sesión cerrada. ¡Hasta pronto!")
            en_menu = False


# ============================================================
# Ejercicio 3 - "Agenda de Turnos con Nombres (sin listas)"
# Contexto: Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
# - Lunes: 4 turnos
# - Martes: 3 turnos
# Reglas:
# 1. Pedir nombre del operador (solo letras).
# 2. Menú repetitivo hasta salir:
#    1. Reservar turno
#    2. Cancelar turno (por nombre)
#    3. Ver agenda del día
#    4. Ver resumen general
#    5. Cerrar sistema
# 3. Reservar:
#    - Elegir día (1=Lunes, 2=Martes).
#    - Pedir nombre del paciente (solo letras).
#    - Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#    - Guardar en el primer espacio libre (ej. lunes1, lunes2...).
# 4. Cancelar:
#    - Elegir día.
#    - Pedir nombre del paciente (solo letras).
#    - Si existe, cancelar y dejar el espacio vacío ("").
# 5. Ver agenda del día:
#    - Mostrar los turnos del día en orden (Turno 1..N), indicando "(libre)" si está vacío.
# 6. Resumen general:
#    - Turnos ocupados y disponibles por día.
#    - Día con más turnos (o empate).
# Restricciones:
# - No listas, no diccionarios, no sets, no tuplas.
# - Se permite usar "" como "vacío".
# - Validaciones con .isalpha() y .isdigit() (sin try/except).
# ============================================================

nombre_operador = input("\nIngrese su nombre (operador): ")
while not nombre_operador.isalpha():
    print("Error: solo se permiten letras.")
    nombre_operador = input("Ingrese su nombre (operador): ")

print(f"Bienvenido/a, {nombre_operador}.")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

sistema_activo = True

while sistema_activo:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Ver resumen general  5) Cerrar sistema")
    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción no válida.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in [1, 2]:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"Error: {paciente} ya tiene un turno reservado el Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno 1 del Lunes reservado para {paciente}.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno 2 del Lunes reservado para {paciente}.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno 3 del Lunes reservado para {paciente}.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno 4 del Lunes reservado para {paciente}.")
            else:
                print("Error: no hay turnos disponibles el Lunes.")

        elif dia == 2:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"Error: {paciente} ya tiene un turno reservado el Martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno 1 del Martes reservado para {paciente}.")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno 2 del Martes reservado para {paciente}.")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno 3 del Martes reservado para {paciente}.")
            else:
                print("Error: no hay turnos disponibles el Martes.")

    elif opcion == 2:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in [1, 2]:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False
        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        elif dia == 2:
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de {paciente} cancelado correctamente.")
        else:
            print(f"Error: no se encontró a {paciente} en ese día.")

    elif opcion == 3:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_str.isdigit() or int(dia_str) not in [1, 2]:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia_str)

        if dia == 1:
            print("\n--- Agenda del Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == 2:
            print("\n--- Agenda del Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print("\n--- Resumen General ---")
        print(f"Lunes   - Ocupados: {ocupados_lunes} | Disponibles: {4 - ocupados_lunes}")
        print(f"Martes  - Ocupados: {ocupados_martes} | Disponibles: {3 - ocupados_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes.")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos ocupados.")

    elif opcion == 5:
        print("Sistema cerrado. ¡Hasta pronto!")
        sistema_activo = False


# ============================================================
# Ejercicio 4 - "Escape Room: La Bóveda"
# Historia: Sos un agente que intenta abrir una bóveda con 3 cerraduras.
# Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado):
# - energia = 100
# - tiempo = 12
# - cerraduras_abiertas = 0
# - alarma = False
# - codigo_parcial = ""
# Validaciones obligatorias:
# - No usar try/except.
# - Pedir nombre del agente y validar con .isalpha() en un while.
# - Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
# Regla anti-spam (muy importante):
# - Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#   se cobra el costo normal (-20 energía, -2 tiempo), NO abre cerradura,
#   y se activa la alarma automáticamente (alarma = True).
# - Si el jugador elige opción 2 o 3, se corta la racha de "forzar seguidas".
# Menú de acciones (se repite mientras el juego siga):
# El juego continúa mientras energia > 0, tiempo > 0, cerraduras_abiertas < 3
# y no esté bloqueado por alarma.
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#    - Si la energía está por debajo de 40, hay "riesgo de alarma":
#      pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#    - Si no hay alarma, abre 1 cerradura.
#    - Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
#    - Debe usar un for de 4 pasos mostrando progreso.
#    - En cada paso sumar una letra al codigo_parcial (por ejemplo "A").
#    - Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
# Regla de bloqueo por alarma:
# - Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
#   se bloquea y se pierde.
# Condiciones de fin:
# - Si cerraduras_abiertas == 3 → VICTORIA
# - Si energia <= 0 o tiempo <= 0 → DERROTA
# - Si se bloquea por alarma → DERROTA (bloqueo)
# ============================================================

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre_agente = input("\nIngrese su nombre de agente: ")
while not nombre_agente.isalpha():
    print("Error: solo se permiten letras.")
    nombre_agente = input("Ingrese su nombre de agente: ")

print(f"\nBienvenido/a, Agente {nombre_agente}. ¡Buena suerte!")

juego_activo = True

while juego_activo:
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n⚠ SISTEMA BLOQUEADO: alarma activa con tiempo crítico.")
        print("DERROTA (bloqueo). La bóveda quedó sellada.")
        juego_activo = False
        break

    if cerraduras_abiertas == 3:
        print(f"\n✅ ¡VICTORIA! Las 3 cerraduras fueron abiertas, Agente {nombre_agente}.")
        juego_activo = False
        break
    if energia <= 0:
        print("\n❌ DERROTA: te quedaste sin energía.")
        juego_activo = False
        break
    if tiempo <= 0:
        print("\n❌ DERROTA: se acabó el tiempo.")
        juego_activo = False
        break

    print(f"\n--- Estado | Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'} ---")
    print("1) Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) Hackear panel    (-10 energía, -3 tiempo)")
    print("3) Descansar        (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar >= 3:
            print("⚠ La cerradura se trabó por el uso excesivo. ¡Alarma activada!")
            alarma = True
            racha_forzar = 0
        else:
            if energia < 40:
                print("⚠ Energía baja: riesgo de alarma.")
                num_str = input("Ingrese un número del 1 al 3: ")
                while not num_str.isdigit() or int(num_str) < 1 or int(num_str) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    num_str = input("Ingrese un número del 1 al 3: ")
                if int(num_str) == 3:
                    alarma = True
                    print("¡La alarma se activó!")
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura forzada. Cerraduras abiertas: {cerraduras_abiertas}/3.")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura forzada. Cerraduras abiertas: {cerraduras_abiertas}/3.")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0
        print("Hackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 - Código parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código completo! Cerradura abierta. Cerraduras abiertas: {cerraduras_abiertas}/3.")

    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activa: se pierden 10 puntos de energía extra durante el descanso.")
        print(f"Descansaste. Energía actual: {energia}.")


# ============================================================
# Ejercicio 5 - "Escape Room: La Arena del Gladiador"
# Descripción del Escenario:
# Vas a desarrollar un simulador de batalla por turnos en Python.
# El programa enfrentará a un usuario (Gladiador) contra un oponente
# controlado por la computadora (Enemigo). El objetivo es reducir los
# puntos de vida del oponente a cero antes de que él lo haga contigo.
# Este ejercicio evalúa el uso de variables (int, float, string, boolean),
# estructuras de control (if/elif/else), ciclos (while y for) y validación
# de datos estricta.
# Tipos de Datos obligatorios:
# - String: Para el nombre del jugador.
# - Int: Para los Puntos de Vida (HP) y cantidad de pociones.
# - Float: Para el cálculo del daño (golpe crítico multiplica el ataque por 1.5).
# - Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
# Reglas de Validación:
# - No está permitido usar bloques try/except.
# - Para validar texto, usar .isalpha() dentro de un ciclo while.
# - Para validar números, usar .isdigit() dentro de un ciclo while.
# Variables iniciales (sin preguntar al usuario):
# - Vida del Gladiador: 100 (int)
# - Vida del Enemigo: 100 (int)
# - Pociones de Vida: 3 (int)
# - Daño base "Ataque Pesado": 15 (int)
# - Daño base del enemigo: 12 (int)
# - Turno Gladiador: True (boolean)
# Acciones:
# 1. Ataque Pesado: si vida del enemigo < 20 → Golpe Crítico (daño base x 1.5, float).
# 2. Ráfaga Veloz: bucle for de 3 repeticiones, cada una resta 5 HP al enemigo.
# 3. Curar: si hay pociones (> 0) suma 30 HP al jugador y resta 1 poción.
#           si no hay pociones: "¡No quedan pociones!" y el enemigo ataca igual.
# Turno del Enemigo: después de cada acción del jugador, el enemigo resta 12 HP al jugador.
# Fin del juego:
# - Si vida_jugador > 0 → "¡VICTORIA! [Nombre] ha ganado la batalla."
# - Si vida_jugador <= 0 → "DERROTA. Has caído en combate."
# ============================================================

print("\n--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print(f"\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: opción fuera de rango. Ingrese 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5
            print(f"¡GOLPE CRÍTICO! Atacaste al enemigo por {danio_final} puntos de daño!")
        else:
            danio_final = float(danio_pesado)
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")
        vida_enemigo -= int(danio_final)

    elif opcion == 2:
        print(">> ¡Iniciás una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("  > Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print(f"¡Usaste una poción! HP actual: {vida_jugador}. Pociones restantes: {pociones}.")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")