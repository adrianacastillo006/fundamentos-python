'''
Clase:        fundamentos de la programacion
Tema:         Bloques condicionales
Ejercicios:     
El número mágico

Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5.

Año bisiesto

Determina si un año es bisiesto, considerando las reglas gregorianas. Para que un año
sea bisiesto, debe cumplir alguna de las siguientes condiciones:
• Si es divisible por 4.
• Si es divisible por 100 y por 400

Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''



#numero magico 
num_magico=int(input("Coloca un numero:"))
if num_magico % 7==0 and num_magico % 5 !=0:
    print("Magico")
else:
    print("Normal")


#año bisiesto
a=int(input("Coloca un año:"))

if a%4==0:
    print("Bisiesto")
elif a%100==0 and a%400==0:
    print("Bisiesto")
else:
    print("No bisiesto")

