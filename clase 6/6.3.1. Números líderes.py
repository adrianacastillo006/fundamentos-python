
'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Estructuras Iterativas
Ejercicios: 6.3.1. Números líderes
Descripcion:
Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes
   


Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-06-2
Estado:       [ Terminado ]
'''
entrada = input("Escriba los numeros: ")
numeros = list(map(int, entrada.split()))
lideres = []

for i in range(len(numeros) - 1):  # no incluye el último
    if numeros[i] > max(numeros[i + 1:]):
        lideres.append(numeros[i])
respuesta=" ".join(str(n) for n in lideres)
print(f"Los numero lideres son:{respuesta}")





       
        
            





