import unittest

from app.modules.costoenvio.CostoEnvioDAO import CostoEnvioDAO
from app.modules.costoenvio.CostoEnvioService import CostoEnvioService


class CostoEnvioDAOFake(CostoEnvioDAO):

    def __init__(self) -> None:
        super().__init__()
        self.costo_actualizado = False

    def obtener(self, pais):
        return 80

    def actualizar(self, pais, costo):
        self.costo_actualizado = True
    
    def actualizar_stock(self, pais, stock):
        self.stock_actualizado = True


class TestCostoEnvioService(unittest.TestCase):

    def test_calcular_pesoMenorAlMaximo_costoIgualCostoPais(self):
        costo_envio_service = CostoEnvioService(CostoEnvioDAOFake())

        costo = costo_envio_service.calcular("Peru", 1)

        self.assertEqual(80, costo)

    def test_actualizarCosto_costoValido_grabaCosto(self):
        costo_envio_dao = CostoEnvioDAOFake()
        costo_envio_service = CostoEnvioService(costo_envio_dao)

        costo_envio_service.actualizar_costo("Peru", 50)

        self.assertTrue(costo_envio_dao.costo_actualizado)

    def test_actualizarStock_pass(self):
        costo_envio_service = CostoEnvioService(CostoEnvioDAOFake())

        costo_envio_service.actualizar_stock("Argentina", 150)

        self.assertTrue(costo_envio_service.actualizar_stock)

if __name__ == '__main__':
    unittest.main()
