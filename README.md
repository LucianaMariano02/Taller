SISTEMA DE EVALUACIÓN DE PROYECTOS ESTUDIANTILES

DESCRIPCIÓN

Este proyecto implementa un sistema que procesa las estadísticas de los equipos en 5 rondas de evaluación.
El programa calcula los puntajes, determina el Mejor Equipo de la Ronda (MER), acumula los resultados y 
muestra una tabla con el ranking general de los equipos.

ESTRUCTURA DEL REPOSITORIO

Taller/ → repositorio principal.
  |
   notebooks/ → contiene:
     |
      src/ → con las funciones principales.
       | 
        evaluaciones.py -> dato de entrada.
        scorin.py -> funciones definidas.
     |
      actividad1.ipynb  -> programa principal.


REQUISITOS

   Python 3.12.9
   Solo se utilizan módulos estándar de Python, no es necesario instalar librerías externas.


RESULTADOS ESPERADOS

   EL PROGRAMA MUESTRA:
     Puntajes de cada equipo en cada ronda.
     El Mejor Equipo de la Ronda (MER). 
     Tablas acumuladas que permiten seguir la evolución del ranking.
     La tabla final con el ranking definitivo de los equipos.