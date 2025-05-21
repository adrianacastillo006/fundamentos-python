'''
Clase:        fundamentos de la programacion
Tema:         Bloques condicionales
Ejercicio:     Cálculo de impuesto
Descripcion: Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
tabla

Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''

#calculo de impuesto,miercoles 14 de mayo 
consumidas=int(input("unidades consumidas:"))
if consumidas <=100:
    print(consumidas)
if consumidas <=200:
    print(f"El  impuesto aplicado es:${consumidas}*0.5")
if consumidas >200:
    print(f"El  impuesto aplicado es: ${consumidas*0.7}")   
