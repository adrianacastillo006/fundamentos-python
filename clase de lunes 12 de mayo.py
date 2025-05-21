'''
Clase:        fundamentos de la programacion
Tema:         variables,tipos,entradas y salidas
Ejercicio:    automatizando el calculo de una propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar.

Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-12
Estado:       [ Terminado ]
'''



cuenta=int(input("Total de su encuenta es: "))
propina_dan=input("el porcentaje que dara: ")

porcentaje= cuenta * int(propina_dan) /100

total_cuenta=cuenta + porcentaje

print(f"Total de le cuenta es:${cuenta}")            
print(f"Propina:${porcentaje}")     
print(f"Total de la cuenta con la propina ({propina_dan}% ) :${total_cuenta}") 