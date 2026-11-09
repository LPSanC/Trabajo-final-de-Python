import unittest


# PUNTO A: CALCULO DE EMISIONES DE CARBONO

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):

    # Validar que el consumo no sea negativo
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")

    # Calcular las emisiones
    emisiones = consumo_kwh * factor_emision

    return emisiones


# PUNTO A: PRUEBAS UNITARIAS

class TestCalculoEmisiones(unittest.TestCase):

    # Prueba 1: Consumo normal
    def test_consumo_normal(self):

        resultado = calcular_emisiones_carbono(100)

        self.assertAlmostEqual(resultado, 40.0)

    # Prueba 2: Consumo igual a cero
    def test_consumo_cero(self):

        resultado = calcular_emisiones_carbono(0)

        self.assertAlmostEqual(resultado, 0.0)

    # Prueba 3: Factor de emision personalizado
    def test_factor_personalizado(self):

        resultado = calcular_emisiones_carbono(200, 0.5)

        self.assertAlmostEqual(resultado, 100.0)

    # Prueba 4: Consumo negativo
    def test_consumo_negativo(self):

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


# PUNTO B: PROCESAMIENTO DE METRICAS

def obtener_metricas_consumo(registros):

    total_emisiones = 0.0
    planta_mayor_consumo = None
    consumo_maximo = -1

    # Recorrer los registros
    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        # Calcular emisiones
        emisiones = calcular_emisiones_carbono(consumo)

        # Acumular emisiones
        total_emisiones += emisiones

        # Identificar la planta de mayor consumo
        if consumo > consumo_maximo:

            consumo_maximo = consumo
            planta_mayor_consumo = planta

    # Devolver resultados
    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo
    }


# PUNTO B: VISTA WEB CON DJANGO

def vista_panel_sustentabilidad(request):

    from django.shortcuts import render

    # Historial de consumos industriales
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 100},
        {"planta": "Planta Sur", "consumo_kwh": 250},
        {"planta": "Planta Este", "consumo_kwh": 150}
    ]

    # Obtener las metricas
    contexto = obtener_metricas_consumo(registros)

    # Enviar los resultados a la plantilla HTML
    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )


# PRUEBA ADICIONAL DE METRICAS

class TestMetricasConsumo(unittest.TestCase):

    def test_metricas(self):

        registros = [
            {"planta": "Planta Norte", "consumo_kwh": 100},
            {"planta": "Planta Sur", "consumo_kwh": 250},
            {"planta": "Planta Este", "consumo_kwh": 150}
        ]

        resultado = obtener_metricas_consumo(registros)

        self.assertAlmostEqual(
            resultado["total_emisiones"],
            200.0
        )

        self.assertEqual(
            resultado["planta_mayor_consumo"],
            "Planta Sur"
        )


# BLOQUE PRINCIPAL DE EJECUCION

if __name__ == "__main__":

    print("=== ECOTECH SOLUTIONS ===")
    print("AUDITORIA DE EMISIONES DE CARBONO")

    # Crear registros de prueba
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 100},
        {"planta": "Planta Sur", "consumo_kwh": 250},
        {"planta": "Planta Este", "consumo_kwh": 150}
    ]

    # Procesar las metricas
    metricas = obtener_metricas_consumo(registros)

    print("\n=== REPORTE DE SUSTENTABILIDAD ===")

    print(
        f"Total global de emisiones: "
        f"{metricas['total_emisiones']:.2f} kg CO2e"
    )

    print(
        f"Planta de mayor consumo: "
        f"{metricas['planta_mayor_consumo']}"
    )

    # Ejecutar pruebas unitarias
    print("\n=== PRUEBAS UNITARIAS ===")

    unittest.main(
        argv=[""],
        exit=False,
        verbosity=2
    )
