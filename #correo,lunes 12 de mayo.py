'''
Clase:        fundamentos de la programacion
Tema:         variables,tipos,entradas y salidas
Ejercicio:   generador correo de key 
descripcion:Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-05-12
Estado:       [ Terminado ]
'''

#correo,lunes 12 de mayo 
#split divide cada palabra de mi string//lo hace una lista
nombre=input("Escriba su nombre completo:")
correo=nombre.split()
nombre_correo=correo[0].lower()
apellido=correo[2].lower()
print(f"Su correo es:{nombre_correo}.{apellido}@keyinstitute.edu.sv ")

