# ============================================================
#  PROGRAMACIÓN 1 Pablo Peralta
#  Trabajo Práctico 2: Estructuras Condicionales
# ============================================================


# ============================================================
# Ejercicio 1
# Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje
# en pantalla que diga "Es mayor de edad".
# ============================================================

edad = int(input("Por favor, ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# ============================================================
# Ejercicio 2
# Escribir un programa que solicite su nota al usuario.
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla
# un mensaje que diga "Aprobado"; en caso contrario deberá
# mostrar el mensaje "Desaprobado".
# ============================================================

nota = float(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# ============================================================
# Ejercicio 3
# Escribir un programa que permita ingresar solo números pares.
# Si el usuario ingresa un número par, imprimir por pantalla el
# mensaje "Ha ingresado un número par"; en caso contrario,
# imprimir "Por favor, ingrese un número par".
# ============================================================

numero = int(input("Por favor, ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# ============================================================
# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima
# por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.
# ============================================================

edad = int(input("Por favor, ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# ============================================================
# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre
# 8 y 14 caracteres (incluyendo 8 y 14). Si la contraseña tiene
# longitud adecuada, imprimir "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir el mensaje de error correspondiente.
# ============================================================

contrasena = input("Por favor, ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# ============================================================
# Ejercicio 6
# Escribir un programa que solicite al usuario el consumo mensual
# de energía eléctrica en kWh e indique la categoría del consumo:
# Menor que 150 kWh: "Consumo bajo".
# Entre 150 y 300 kWh (inclusive): "Consumo medio".
# Mayor que 300 kWh: "Consumo alto".
# Además, si el consumo supera los 500 kWh, mostrar un mensaje
# adicional: "Considere medidas de ahorro energético".
# ============================================================

consumo = float(input("Por favor, ingrese su consumo mensual en kWh: "))
if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")


# ============================================================
# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de
# exclamación al final e imprimir el string resultante; en caso
# contrario, dejar el string tal cual e imprimirlo por pantalla.
# ============================================================

frase = input("Por favor, ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)


# ============================================================
# Ejercicio 8
# Escribir un programa que solicite al usuario su nombre y el
# número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Nombre en mayúsculas. Ejemplo: PEDRO.
# 2. Nombre en minúsculas. Ejemplo: pedro.
# 3. Nombre con la primera letra mayúscula. Ejemplo: Pedro.
# ============================================================

nombre = input("Por favor, ingrese su nombre: ")
opcion = int(input("Elija una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera letra mayúscula): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


# ============================================================
# Ejercicio 9
# Escribir un programa que pida al usuario la magnitud de un
# terremoto y clasifique la magnitud según la escala de Richter:
# Menor que 3: "Muy leve" (imperceptible).
# Entre 3 y 4: "Leve" (ligeramente perceptible).
# Entre 4 y 5: "Moderado" (sentido por personas, no causa daños).
# Entre 5 y 6: "Fuerte" (puede causar daños en estructuras débiles).
# Entre 6 y 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (graves daños a gran escala).
# ============================================================

magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# ============================================================
# Ejercicio 10
# Escribir un programa que pregunte al usuario en cuál hemisferio
# se encuentra (N/S), qué mes del año es y qué día es. El programa
# deberá imprimir por pantalla si el usuario se encuentra en
# otoño, invierno, primavera o verano, según la tabla de estaciones.
# ============================================================

hemisferio = input("Por favor, ingrese su hemisferio (N/S): ").upper()
mes = int(input("Por favor, ingrese el mes actual (1-12): "))
dia = int(input("Por favor, ingrese el día actual: "))

# Determinamos el período estacional según mes y día
if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    periodo = "A"  # 21 dic - 20 mar
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    periodo = "B"  # 21 mar - 20 jun
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    periodo = "C"  # 21 jun - 20 sep
else:
    periodo = "D"  # 21 sep - 20 dic

if hemisferio == "N":
    if periodo == "A":
        print("Invierno")
    elif periodo == "B":
        print("Primavera")
    elif periodo == "C":
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if periodo == "A":
        print("Verano")
    elif periodo == "B":
        print("Otoño")
    elif periodo == "C":
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio no válido. Por favor, ingrese N o S.")