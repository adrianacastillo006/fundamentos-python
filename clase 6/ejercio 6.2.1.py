#tarea 9/practica de lista
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

