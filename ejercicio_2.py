
import json


# EJERCICIO 2 - ECOTECH SOLUTIONS
# Modelo de productos, excepciones y persistencia


# PUNTO A: Excepcion personalizada
class StockInvalidoError(Exception):
    pass


# Clase base: Dispositivo Ecologico
class DispositivoEcológico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

    # Encapsulamiento del stock
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, cantidad):
        if cantidad < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo"
            )
        self._stock = cantidad

    # Ficha tecnica general
    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    # Convertir objeto a diccionario
    def a_diccionario(self):
        return {
            "tipo": "DispositivoEcológico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }


# Clase hija: Panel Solar
class PanelSolar(DispositivoEcológico):

    def __init__(self, nombre, precio, stock,
                 potencia_watts, eficiencia):

        super().__init__(nombre, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    # Polimorfismo: ficha personalizada
    def ficha_tecnica(self):
        return (
            f"{super().ficha_tecnica()} | "
            f"Potencia: {self.potencia_watts} W | "
            f"Eficiencia: {self.eficiencia}%"
        )

    def a_diccionario(self):
        datos = super().a_diccionario()

        datos["tipo"] = "PanelSolar"
        datos["potencia_watts"] = self.potencia_watts
        datos["eficiencia"] = self.eficiencia

        return datos


# PUNTO B: Gestion del inventario
class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos,
                              ruta_archivo):

        datos = []

        for dispositivo in lista_dispositivos:
            datos.append(dispositivo.a_diccionario())

        with open(ruta_archivo, "w",
                  encoding="utf-8") as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )


# BLOQUE PRINCIPAL DE PRUEBA
if __name__ == "__main__":

    # Crear productos
    panel = PanelSolar(
        "Panel Solar Eco 400",
        250000,
        12,
        400,
        21.5
    )

    lampara = DispositivoEcológico(
        "Lampara LED Ecologica",
        15000,
        30
    )

    # Probar un stock incorrecto
    try:
        panel.stock = -5

    except StockInvalidoError as error:
        print("Error controlado:", error)

    # Crear catalogo valido
    catalogo = [panel, lampara]

    # Mostrar fichas tecnicas
    print("\n=== CATALOGO ECOTECH ===")

    for producto in catalogo:
        print(producto.ficha_tecnica())

    # Guardar los productos en JSON
    gestor = GestorInventario()

    gestor.guardar_catalogo_json(
        catalogo,
        "catalogo_ecotech.json"
    )

    print("\nCatalogo guardado correctamente")
    print("Archivo: catalogo_ecotech.json")


    print(
        "Catálogo guardado correctamente "
        "en catalogo_ecotech.json"
    )
