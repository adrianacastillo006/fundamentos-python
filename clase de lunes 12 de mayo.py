cuenta=int(input("Total de su encuenta es: "))
propina_dan=input("el porcentaje que dara: ")

porcentaje= cuenta * int(propina_dan) /100

total_cuenta=cuenta + porcentaje

print(f"Total de le cuenta es:${cuenta}")            
print(f"Propina:${porcentaje}")     
print(f"Total de la cuenta con la propina ({propina_dan}% ) :${total_cuenta}") 