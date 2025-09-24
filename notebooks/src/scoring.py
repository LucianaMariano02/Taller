
def puntaje_equipo(puntaje):
    """
     Calculo el puntaje de cada equipo en cada ronda.
    """
    puntos_innovacion = 3 * puntaje['innovacion']
    puntos_presentacion = puntaje['presentacion']
    penalizacion_error = 1 if puntaje['errores'] else 0
    puntaje_total = puntos_innovacion + puntos_presentacion - penalizacion_error

    return puntaje_total


def puntaje_ronda(ronda):
    """
    Devuelve un diccionario con los puntajes de todos los equipos de una ronda
    """
    equipos_data = ronda.items()
    pares = []
    for equipo, data in equipos_data:
        puntaje = puntaje_equipo(data) 
        pares.append((equipo,puntaje))
    return dict(pares)  

def mejor_equipo_ronda(puntajes):
    """
    Encuentra el mejor equipo de una ronda
    """
    mejor = None
    for equipo, puntaje in puntajes.items():
        if mejor is None or puntaje > mejor[1]:   
            mejor = (equipo, puntaje)
    return mejor

def mantener_acumulado (acumulado,ronda,equipo_mer):
    """
    Inicializa y actualiza el acumulado con los valores de la ronda.
    """

    for equipo,data in ronda.items():
        if equipo not in acumulado:
            acumulado[equipo] = {
                "innovacion":0,
                "presentacion":0,
                "errores":0,
                "mer":0,
                "total":0,
            }
        acumulado[equipo]["innovacion"] += data["innovacion"]
        acumulado[equipo]["presentacion"] += data["presentacion"]
        acumulado[equipo]["errores"] += 1 if list(filter(lambda x: x is True, [data["errores"]])) else 0
        points = puntaje_equipo(data)
        acumulado[equipo]["total"] += points
    acumulado[equipo_mer]["mer"] += 1

    return acumulado

