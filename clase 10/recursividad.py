#clase 11 de junio 2024/recursividad 
#crear una funcion que muestre una cuenta  5...4...3...2...1..!listo!
import time

def cuenta_rregresiva_iterativa(n):
    for i in range(n,0,-1):
        #lo que se hace que es de n hasta 0,restandole a n una unidad(-1)
        print(i,end='...')
        #time.sleep(0.5)
    print("Despegue!")

cuenta_rregresiva_iterativa(12)


def cuenta_regresiva_recursiva(n):
    if n<=0:
         print("Despegue!")
    else:
        print(n,end="...")
        #time.sleep(0.5)
        cuenta_regresiva_recursiva(n-1)

cuenta_regresiva_recursiva(10)


#crear  dos funciones (iterativas y recursivsas) que genere y devuelva el abecedario

def generar_alfabeto_iterativo():
    alfabeto = ''
    letra = 'a'
    for i in range(ord('a'),ord('z')+1,1):
        alfabeto+=chr(i) +','#chr de num a letra
    alfabeto=alfabeto.rstrip(',')#elimina la ultima coma
    return alfabeto
print(generar_alfabeto_iterativo())

#iteracion 
def generar_alfabeto_recursivo(letra):
    if letra =='z':
        return 'z'
    return letra +","+generar_alfabeto_recursivo(chr(ord(letra)+1))#ord de letras a numeros 
print(generar_alfabeto_recursivo('a'))


#crear una funcion para calcular el factorial de un numero 
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))




'Crear una funcion que cuente recursivamente los vecionos en una matriz binaria,'
'condicion:contrar vecinos que se encuentre horizontal y vertical'

def 


