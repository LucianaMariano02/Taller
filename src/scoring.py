from typing import Dict

def puntaje_equipo(param):
    
# Calculo el puntaje de cada equipo en cada ronda:
# +3 puntos por cada punto de innovación.
# +1 punto por cada punto de presentación.
# -1 punto si tuvo errores graves (True).

    # variable auxiliar para innovación
    puntos_innovacion = 3 * param['innovacion']
    # variable auxiliar para presentación
    puntos_presentacion = param['presentacion']
    # variable auxiliar para errores (1 si hay error, 0 si no)
    penalizacion_error = 1 if param['errores'] else 0
    # suma final
    puntaje_total = puntos_innovacion + puntos_presentacion - penalizacion_error

    return puntaje_total
