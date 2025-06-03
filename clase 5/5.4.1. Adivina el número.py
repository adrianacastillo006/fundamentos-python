#5.4.1. Adivina el número.py
'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Estructuras Iterativas
Ejercicios: 5.4.1. ¡Adivina el número!
Descripcion:
Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.
Entrada:
• Números enteros entre 1 y 100.
Salida:
• Tres posibles salidas: “El número secreto es menor”, “El número secreto
es mayor”, ¡Felicidades! Has adivinado el número secreto!”    


Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
import random
secreto=random.randint(1,100)
adivinando=False
while not adivinando:
    intento=int(input("Ingrese un numero entre 1 y 100:"))
    if intento<1 or intento>100:
        intento=int(input("Ingrese un numero entre 1 y 100:"))
        continue
    if intento==secreto:
        adivinando=True
        print("¡Felicidades! Has adivinado el número secreto!")
    if intento < secreto:
        print("El número secreto es mayor")
    if intento > secreto:
         print("El número secreto es menor")
   



