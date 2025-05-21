
'''
Clase:        fundamentos de la programacion
Tema:        bloque condicional
Ejercicio:   Contraseña segura
descripcion: Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''

#casos de exploracion 
#isdigit() method in Python is a built-in string function used to check if all characters in a string are digits (0-9).
#isupper() The isupper() method returns True if all the characters are in upper case
contra=input("ingrese contra:")

mayuscula = False
numero = False


for i in contra:
    if i.isupper():
        #print("contiene masc")
        mayuscula=True
    if i.isdigit():
        #print("contiene digito")
        digito=True 

if mayuscula==True and  digito==True and len(contra)>=8:
    print("Contrasena segura")
else:
    print("Contrasena  no es segura")








