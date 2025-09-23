
def puntaje_equipo(puntaje):
    
# Calculo el puntaje de cada equipo en cada ronda:
# +3 puntos por cada punto de innovación.
# +1 punto por cada punto de presentación.
# -1 punto si tuvo errores graves (True).

    # variable auxiliar para innovación
    puntos_innovacion = 3 * puntaje['innovacion']
    # variable auxiliar para presentación
    puntos_presentacion = puntaje['presentacion']
    # variable auxiliar para errores (1 si hay error, 0 si no)
    penalizacion_error = 1 if puntaje['errores'] else 0
    # suma final
    puntaje_total = puntos_innovacion + puntos_presentacion - penalizacion_error

    return puntaje_total


def puntaje_ronda(ronda):
    #devuelvo todos los elementos de param como pares.
    equipos_data = ronda.items()
    #creo una lista vacia para guardar los pares (equipo,puntaje)
    pares = []
    #recorro todos los pares dentro de equipos_stats
    for equipo, data in equipos_data:
        puntaje = puntaje_equipo(data) #le paso las estadisticas de un equipo.
        pares.append((equipo,puntaje))
    return dict(pares)  #convierto la lista de tuplas a diccionario.

def mejor_equipo_ronda(puntajes):
    mejor = None
    for equipo, puntaje in puntajes.items():
        if mejor is None or puntaje > mejor[1]:   #mejor es una tupla
            mejor = (equipo, puntaje)
    return mejor

def mantener_acumulado (acumulado,ronda,equipo_mer):
    #recorro equipos e inicializo.
    for equipo,data in ronda.items():
        if equipo not in acumulado:
            acumulado[equipo] = {
                "innovacion":0,
                "presentacion":0,
                "errores":0,
                "mer":0,
                "total":0,
            }
        #sumo la innovación al acumulado.
        acumulado[equipo]["innovacion"]=acumulado[equipo]["innovacion"] + data["innovacion"]
        #sumo la presentación al acumulado.
        acumulado[equipo]["presentacion"]=acumulado[equipo]["presentacion"] + data["presentacion"]
        #si hubo errores los cuento.
        acumulado[equipo]["errores"] += 1 if list(filter(lambda x: x is True, [data["errores"]])) else 0
        #calculo el puntaje de la ronda.
        points = puntaje_equipo(data)
        #sumo el puntaje de la ronda al total acumulado.
        acumulado[equipo]["total"] = acumulado[equipo]["total"] + points
    #cuando termino de recorrer los equipos, aumenro el contador del mer (mejor equipo)
    acumulado[equipo_mer]["mer"] = acumulado[equipo_mer]["mer"] + 1

    return acumulado

