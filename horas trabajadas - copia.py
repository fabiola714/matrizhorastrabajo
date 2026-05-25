# Matriz:[NOMBRE, LUNES, MARTES, MIÉRCOLES, JUEVES, VIERNES]
EQUIPO = [
    ["Ana", 8, 7, 8, 9, 8],
    ["Luis", 9, 9, 10, 8, 9],
    ["marta", 7, 8, 7, 8, 7],
    ["pedro", 10, 9, 9, 10, 8]
]

UMBRAL_HORAS = 40
def evaluar_jornada(matriz):
    """
    calcula el total de horas semanales por recurso 
    y clasifica su jornada segun el umbral.
    """
    for persona in matriz:
        nombre = persona[0]
        horas_totales = sum(persona[1:]) # suma de lunes a viernes
        if horas_totales>UMBRAL_HORAS:
            estado = "sobretiempo"
        else:
            
            estado = "horario estandar o inferior"
            
        # salida solicitada
        print(f"{nombre}: {horas_totales} horas - {estado}")
        
# ejecutar funcion  
Evaluar_jornada(equipo)      
    