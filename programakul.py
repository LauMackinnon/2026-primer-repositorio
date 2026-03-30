import random

numero_secreto = random.randint(1, 1000)
intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He seleccionado un número entre 1 y 1000. ¡Adivínalo!")

while True:
    try:
        intento = int(input("Ingresa tu adivinanza: "))
        intentos += 1

        if intento < 1 or intento > 1000:
            print("Por favor, ingresa un número entre 1 y 1000.")
            continue

        if intento < numero_secreto:
            print("Más alto.")
        elif intento > numero_secreto:
            print("Más bajo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")