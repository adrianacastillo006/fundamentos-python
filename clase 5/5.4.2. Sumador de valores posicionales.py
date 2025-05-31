'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Estructuras Iterativas
Ejercicios: 5.4.2. ¡Sumador de valores posicionales!
Descripcion:
Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
Entrada:
• Un numero entero.
Restricciones:
• 1 ≤ número ≤ 10^9
Conceptos explorados:
• Bucles y control de flujo.
16

   


Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

numero=input("Ingrese un numero: ")
print(f"Tu numero es:{numero}")


while len(numero) != 1:

    lista = []

    for i in numero:
        i = int(i)
        lista.append(i)
        suma=sum(lista)
    print(f"{numero}={suma}")
    numero = str(suma)
    



print (f"El resultado final es:{suma}")









