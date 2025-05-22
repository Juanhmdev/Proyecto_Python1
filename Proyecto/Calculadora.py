# ==========================================
# PROYECTO: Calculadora de eficiencia operativa
# ==========================================

# 1. Entrada de datos
# 2. Cálculo del tiempo total
# 3. Cálculo de porcentajes
# 4. Evaluación
# 5. Impresión de resultados


nombre = input("Ingrese el nombre del operador: ")
area = input("Ingrese la área de trabajo: ")
hora_inicio = int(input("Ingrese la hora de inicio de la jornada: "))
hora_fin = int(input("Ingrese la hora de fin de la jornada: "))
minutos_productivos = int(input("Ingrese el número de minutos productivos: "))
minutos_pausa = int(input("Ingrese el número de minutos de pausa: "))
minutos_improductivos = int(input("Ingrese el número de minutos de improductivo: "))

hora_trabajada = (hora_fin - hora_inicio) * 60
tiempo_productivo = (minutos_productivos / hora_trabajada) * 100 
tiempo_pausa = (minutos_pausa / hora_trabajada) * 100
tiempo_improductivos = (minutos_improductivos / hora_trabajada) * 100

if tiempo_productivo < 50:
    evaluacion = "Necesitas mejorar tu enfoque."
elif tiempo_productivo >= 50 and tiempo_productivo < 80:
    evaluacion = "Buen desempeño, pero hay margen de mejora."
elif tiempo_productivo >= 80:
    evaluacion = "Excelente desempeño, sigue así."

print ("========== RESUMEN DE EFICIENCIA OPERATIVA ==========")
print (f"{'Nombre':18}: {nombre}")
print (f"{'Área':18}: {area}")
print (f"{'Jornada(min)':18}: {hora_trabajada}")
print (f"{'Tiempo productivo':18}: {minutos_productivos} min ({tiempo_productivo:.2f}%)")
print (f"{'Pausas tomadas':18}: {minutos_pausa} min ({tiempo_pausa:.2f}%)")
print (f"{'Tiempo perdido':18}: {minutos_improductivos} min ({tiempo_improductivos:.2f}%)")
print (f"\nEvaluación: {evaluacion}")
print ("======================================================")