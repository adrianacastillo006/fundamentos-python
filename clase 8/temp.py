
'''
Clase:        fundamentos de la programacion
Tema:         Fase de fortalecimiento lógico: Manejo de matrices
Ejercicios: 10.3.1. Matriz simétrica
descripcion:
Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.
Entrada:
• Numero entero N con la dimensión de la
matriz. N conjuntos de números enteros
separados por coma.
Salida:
• Una línea con una cadena de texto. “La
matriz es simétrica” si es simétrica; “La
matriz no es simétrica” en caso contrario


Autor:        Adriana Maria Castillo Ramirez
Fecha:        2025-06-12
Estado:       [ Terminado ]
'''

N=int(input())
l=[]
for i in range(N):
    temp=list(map(int,input().split()))
    l.append(temp)

    
diagonal_principal=[]
diagonal_secundaria=[]
for i in range(N):#recorre las filas
    for j in range (len(l[i])):#recorre las columnas 
        #print (F"valor en la posicion ({i},{j}):{l[i][j]}")
     if i==j:
        diagonal_principal.append(l[i][j])
    if i+j ==len(l)-1:
        diagonal_secundaria.append(l[i][j])
        #print(f"el valor en la posicion {i},{j}: {l[i][j]}")
    print(f"La diagonal principal es:{diagonal_principal}")
    print(f"La diagonal secundaria  es:{diagonal_secundaria}")


    