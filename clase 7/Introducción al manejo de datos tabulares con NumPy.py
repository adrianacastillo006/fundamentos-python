import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:",consumo.ndim)
print("Forma:",consumo.shape)
print("Tipo de datos:",consumo.dtype)
print("Consumo primer hogar :",consumo[0])
print("Consumo el miercoles(dia 3):",consumo[:,2])


# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

#suma por hogar(semana)
consumo_total_hogar=np.sum(consumo,axis=1)
# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)
# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")
# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print(consumo_normalizado)





#cuestionario

#pregunta 1
consumo_hogar5=consumo[4,4]
print(f"1. el consumo del hogar 5 el viernes (dia 5) es {consumo_hogar5}")
#pregunta 2
consumo_domimgo=consumo[[7,8,9],6]
print(f"2. el consumo de los ultimos tres lugares el domingo es: {consumo_domimgo} ")
#pregunta 3
datos=consumo[:,[5,6]]
promedio_consumo_finde=np.mean(datos)
print(f"3. el promedio de consumo los fines de semana es: {promedio_consumo_finde :.2f}")

#pregunta 4 
desviacion_dia=np.std(consumo,axis=0)
max_desvi=np.argmax(desviacion_dia)
dias=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
print(f"4. el dia con mayor desviacion estandar es  el {dias[max_desvi]}.Este dia  los hogares no consumieron de forma similar. Algunos consumieron poco, otros mucho.")

#pregunta 5
menor_consumo = np.argsort(consumo_total_hogar)[:3]
valor_menores = consumo_total_hogar[menor_consumo]
print("5. Los tres hogares con menor consumo son:")
for i  in range(len(menor_consumo)):
    print(f"   - Hogar {menor_consumo[i]} con {valor_menores[i]:.2f} unidades de consumo")

#pregunta 6
hogar_3=consumo[2]
porciento=hogar_3*1.10
total=np.sum(porciento)
print(f"6. El nuevo consumo semanal de la casa 3 seria {total:.2f}")