# Hola, este es mi proyecto de mi primer curso de programación. En realidad, yo solo he editado y agregado unas cosas,
# ya que ya venia gran parte realizado. Igualmente, quiero guardarlo para poder revisarlo cuando lo necesite.

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Función para solicitar los datos del usuario
def obtener_datos_usuario():
    nombre = input("Para empezar, dime como te llamas. ")
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = 2025 - agno - 1
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
    return nombre, edad, estatura_m, estatura_cm, num_amigos

# Función para mostrar el perfil del usuario
def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")

# Función para publicar un mensaje
def publicar_mensaje(nombre, mensaje, es_publico=True, num_amigos=0):
    print("--------------------------------------------------")
    if es_publico:
        print(nombre, "dice:", mensaje)
    else:
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
    print("--------------------------------------------------")

# Solicitar los datos iniciales
nombre, edad, estatura_m, estatura_cm, num_amigos = obtener_datos_usuario()
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

# Esta opción permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    # Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        publicar_mensaje(nombre, mensaje)

    # Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        publicar_mensaje(nombre, mensaje, es_publico=False, num_amigos=num_amigos)

    # Código para la opción 3. Mostrar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        print("Vamos a actualizar tu perfil.")
        nombre, edad, estatura_m, estatura_cm, num_amigos = obtener_datos_usuario()
        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
        print()

    # Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    # Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")