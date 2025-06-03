#tarea 9/practica de lista
'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Estructuras Iterativas
Ejercicios:6.2.1. Eliminando valores duplicados
Dada una lista ingresada por el usuario,
elimina los elementos duplicados
manteniendo la primera aparición de cada
número.
Entrada:
• La primera línea contiene n enteros a₁, ...,
aₙ (1 ≤ aᵢ ≤ 10⁶)
Salida:
• Una línea con los enteros únicos en su
orden de aparición, separados por
espacios.
10


Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

entrada=input("pon numeros:")
lista=entrada.split()
nueva=[]
for i in lista:
    if i not in nueva:
        nueva.append(i)
    else:
        pass
respuesta=" ".join(nueva)
print(respuesta)

