import random
def obtener_datos_trafico():
    flujo_vehicular = random.randint(10, 150)
    densidad_via = random.randint(5, 100)
    return {"flujo": flujo_vehicular, "densidad": densidad_via}
def calcular_tiempo_semaforo(datos):
    flujo = datos["flujo"]
    densidad = datos["densidad"]
    tiempo_verde = 30
    if flujo > 90 or densidad > 70:
        tiempo_verde += 25
    elif flujo < 30:
        tiempo_verde -= 10
    return tiempo_verde
def test_algoritmo_control():
    datos_criticos = {"flujo": 120, "densidad": 85}
    resultado = calcular_tiempo_semaforo(datos_criticos)
    assert resultado > 30, "Error: El algoritmo no aumento el tiempo en hora punta."
    print("Prueba del Modulo de Control: PASADA")
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE CONTROL VIAL DE LA JAVIER PRADO ---")
    test_algoritmo_control()
    datos_actuales = obtener_datos_trafico()
    tiempo_asignado = calcular_tiempo_semaforo(datos_actuales)
    print(f"Datos capturados -> Flujo: {datos_actuales['flujo']} autos/min, Densidad: {datos_actuales['densidad']}%%")
    print(f"Resultado de la IA -> Tiempo asignado a luz verde: {tiempo_asignado} segundos.")
