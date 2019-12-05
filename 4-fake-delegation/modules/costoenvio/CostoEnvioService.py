from .CostoEnvioDAO import CostoEnvioDAO

class CostoEnvioService:

    def __init__(self, CostoEnvioDAO):
        self.peso_maximo = 8.5
        self.costo_envio_dao = CostoEnvioDAO

    def calcular(self, pais, peso):
        costo_x_peso = 0
        if peso > self.peso_maximo:
            costo_x_peso = peso - self.peso_maximo

        costo_x_distancia = self.obtener_costo_pais(pais)

        return costo_x_peso + costo_x_distancia

    def actualizar_costo(self, pais, costo):
        if costo == 0:
            raise Exception("Costo envio no puede ser 0")

        self.grabar_costo(costo, pais)

    def obtener_costo_pais(self, pais):
        return self.costo_envio_dao.obtener(pais)

    def grabar_costo(self, costo, pais):
        self.costo_envio_dao.actualizar(pais, costo)

    def actualizar_stock(self, pais, stock):
        self.costo_envio_dao.actualizar_stock(pais, stock)

