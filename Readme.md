🧾 Proyecto Integrador – Módulo 1
Nombre del archivo: proyecto_calculadora_operativa.py
Nombre del proyecto: Calculadora de Eficiencia Operativa Diaria

🎯 Objetivo:
Crear una aplicación de consola que permita a un usuario calcular su eficiencia operativa 
diaria según su jornada laboral, considerando tiempos activos, pausas, tiempos muertos y 
tiempos improductivos.

📚 Contexto del problema:
Eres el responsable de controlar y mejorar la productividad de tu jornada de trabajo 
(ejemplo: en obras públicas o estudio). Necesitas tener una herramienta que te permita 
ingresar los datos de tu jornada diaria y calcular qué porcentaje fue realmente productivo, 
ayudándote a reflexionar sobre cómo mejorar.

📂 Requisitos funcionales:
Solicita al usuario los siguientes datos:

- Su nombre y área de trabajo
- Hora de inicio y fin de jornada (en formato horas)
- Total de minutos productivos (tareas efectivas)
- Total de minutos en pausas programadas (descanso/lonche)
- Total de minutos improductivos (distracciones, interrupciones)

Calcula automáticamente:

1. Tiempo total trabajado en minutos
2. Porcentaje de tiempo productivo
3. Porcentaje de tiempo en pausas
4. Porcentaje de tiempo improductivo
5. Una evaluación textual según su eficiencia:
🔴 Menos de 50% → "Necesitas mejorar tu enfoque."
🟡 Entre 50% y 80% → "Buen desempeño, pero hay margen de mejora."
🟢 Más de 80% → "Excelente nivel de productividad."
6. Muestra todos los resultados en una tabla de resumen clara y ordenada (estilo terminal).

🧰 Restricciones técnicas:
- Solo debes usar funciones del Módulo 1 (variables, input, print, if, operaciones, tipos, f-strings).
- No usar librerías externas.
- Aplica estilo PEP8 y comentarios adecuados.

======= RESUMEN DE EFICIENCIA OPERATIVA =======
Nombre           : Juan Andrés
Área             : Oficina Técnica
Jornada (min)    : 480
Tiempo productivo: 360 min (75.0%)
Pausas tomadas   : 60 min (12.5%)
Tiempo perdido   : 60 min (12.5%)

Evaluación: Buen desempeño, pero hay margen de mejora.
===============================================
