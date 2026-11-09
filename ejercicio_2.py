
import json


# PUNTO A: Excepción personalizada
class StockInvalidoError(Exception):
    pass


# Clase base
class DispositivoEcológico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

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

    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def a_diccionario(self):
        return {
            "tipo": "DispositivoEcológico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }


# Clase hija: Herencia y polimorfismo
class PanelSolar(DispositivoEcológico):

    def __init__(self, nombre, precio, stock,
                 potencia_watts, eficiencia):

        super().__init__(nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

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


# PUNTO B: Persistencia en JSON
class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos,
                              ruta_archivo):

        datos = [
            dispositivo.a_diccionario()
            for dispositivo in lista_dispositivos
        ]

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

    panel = PanelSolar(
        "Panel Solar Eco 400",
        250000,
        12,
        400,
        21.5
    )

    dispositivo = DispositivoEcológico(
        "Lámpara LED Ecológica",
        15000,
        30
    )

    # Prueba de stock negativo
    try:
        panel.stock = -5

    except StockInvalidoError as error:
        print("Error controlado:", error)

    # Catálogo de productos válidos
    catalogo = [panel, dispositivo]

    for producto in catalogo:
        print(producto.ficha_tecnica())

    # Guardar archivo JSON
    gestor = GestorInventario()

    gestor.guardar_catalogo_json(
        catalogo,
        "catalogo_ecotech.json"
    )

    print(
        "Catálogo guardado correctamente "
        "en catalogo_ecotech.json"
    )
