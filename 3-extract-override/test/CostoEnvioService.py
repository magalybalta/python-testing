import unittest

from app.modules.costoenvio.CostoEnvioService import CostoEnvioService


class TestableCostoEnvioService(CostoEnvioService):

    def __init__(self):
        super().__init__()
        self.costo_grabado = False

    def obtener_costo_pais(self, pais):
        return 80

    def grabar_costo(self, costo, pais):
        self.costo_grabado = True

    def exportar_merca(self, precio):
        self.merca = precio 


class TestCostoEnvioService(unittest.TestCase):

    def test_calcular_pesoMenorAlMaximo_costoIgualCostoPais(self):
        costo_envio_service = TestableCostoEnvioService()

        costo = costo_envio_service.calcular("Peru", 1)

        self.assertEqual(80, costo)

    def test_actualizarCosto_costoValido_grabaCosto(self):
        costo_envio_service = TestableCostoEnvioService()

        costo_envio_service.actualizar_costo("Peru", 50)

        self.assertTrue(costo_envio_service.costo_grabado)
    
    def test_exportarMerca_pass(self):
        costo_envio_service = TestableCostoEnvioService()
        
        precio = 100

        costo_envio_service.exportar_merca(precio)

        self.assertEqual(costo_envio_service.merca, 100)




if __name__ == '__main__':
    unittest.main()
