import unittest

from modules.costoenvio.CostoEnvioService import CostoEnvioService


class TestableCostoEnvioService(CostoEnvioService):

    def __init__(self):
        super().__init__()
        self.costo_grabado = False

    def obtener_costo_pais(self, pais):
        return 80

    def grabar_costo(self, costo, pais):
        self.costo_grabado = False


class TestCostoEnvioService(unittest.TestCase):

    def test_calcular_pesoMenorAlMaximo_costoIgualCostoPais(self):
        costo_envio_service = TestableCostoEnvioService()

        costo = costo_envio_service.calcular("Peru", 1)

        self.assertEqual(80, costo)

    def test_actualizarCosto_costoValido_grabaCosto(self):
        costo_envio_service = TestableCostoEnvioService()

        costo_envio_service.actualizar_costo("Peru", 50)

        self.assertTrue(costo_envio_service.costo_grabado)


if __name__ == '__main__':
    unittest.main()
