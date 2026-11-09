
# TRABAJO FINAL - EJERCICIO 1
# Sanitización y análisis estadístico de sensores


# PUNTO A: Normalización de registros

def limpiar_registro_sensor(registro_raw):

    sensor_id = registro_raw["sensor_id"].strip()

    temperatura = float(
        registro_raw["temperatura"].strip().replace("C", "")
    )

    ubicacion = registro_raw.get("ubicacion", "Desconocida")

    if not ubicacion or not ubicacion.strip():
        ubicacion = "Desconocida"
    else:
        ubicacion = ubicacion.strip()

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


# PUNTO B: Resumen estadístico

def generar_resumen_sensores(lista_sensores_limpios,
                             umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]
        suma_temperaturas += temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    cantidad = len(lista_sensores_limpios)

    if cantidad > 0:
        promedio_temperatura = suma_temperaturas / cantidad
    else:
        promedio_temperatura = 0.0

    return (lista_sensores_alerta, promedio_temperatura)


# BLOQUE PRINCIPAL

sensores_crudos = [
    {"sensor_id": " SENSOR-001 ",
     "temperatura": "24.5C",
     "ubicacion": "Planta Norte"},

    {"sensor_id": " SENSOR-002 ",
     "temperatura": "35.2C"},

    {"sensor_id": " SENSOR-003 ",
     "temperatura": "28.0C",
     "ubicacion": "Planta Sur"},

    {"sensor_id": " SENSOR-004 ",
     "temperatura": "32.3C",
     "ubicacion": " "}
]

# Limpiar todos los registros
sensores_limpios = []

for registro in sensores_crudos:
    sensor_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(sensor_limpio)

# Generar el reporte
umbral = 30

alertas, promedio = generar_resumen_sensores(
    sensores_limpios, umbral
)

print("=== REPORTE DE SENSORES ===")

print("\nRegistros normalizados:")
for sensor in sensores_limpios:
    print(sensor)

print(f"\nUmbral de temperatura: {umbral} °C")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Sensores en alerta: {alertas}")
