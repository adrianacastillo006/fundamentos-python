#tarea 9/practica de lista
'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Estructuras Iterativas
Ejercicios: 6.3.1. Números líderes
Descripcion:
Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.


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

