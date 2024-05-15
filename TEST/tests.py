import unittest
from GrafoLogistica import GrafoLogistica

class TestGrafoLogistica(unittest.TestCase):
    def setUp(self):
        # Creamos un grafo de prueba para usar en las pruebas
        self.grafo_prueba = {
            'BuenosAires': {'SaoPaulo': {'normal': 10, 'lluvia': 15, 'nieve': 20, 'tormenta': 50},
                            'Lima': {'normal': 15, 'lluvia': 20, 'nieve': 30, 'tormenta': 70}},
            'SaoPaulo': {'BuenosAires': {'normal': 10, 'lluvia': 15, 'nieve': 20, 'tormenta': 50}},
            'Lima': {'BuenosAires': {'normal': 15, 'lluvia': 20, 'nieve': 30, 'tormenta': 70},
                     'Quito': {'normal': 10, 'lluvia': 12, 'nieve': 15, 'tormenta': 20}},
            'Quito': {'Lima': {'normal': 10, 'lluvia': 12, 'nieve': 15, 'tormenta': 20}}
        }

    def test_leer_archivo(self):
        grafo_logistica = GrafoLogistica("logistica.txt")
        self.assertEqual(grafo_logistica.grafo, self.grafo_prueba)

    def test_ruta_mas_corta(self):
        grafo_logistica = GrafoLogistica("logistica.txt")
        # Prueba para la ruta más corta entre dos ciudades
        self.assertEqual(grafo_logistica.ruta_mas_corta("BuenosAires", "Lima"), ["BuenosAires", "Lima"])
        # Prueba para la misma ciudad como origen y destino
        self.assertEqual(grafo_logistica.ruta_mas_corta("BuenosAires", "BuenosAires"), ["BuenosAires"])
        # Prueba para ciudades no conectadas
        self.assertEqual(grafo_logistica.ruta_mas_corta("BuenosAires", "Quito"), ["BuenosAires", "Lima", "Quito"])

    def test_centro_del_grafo(self):
        grafo_logistica = GrafoLogistica("logistica.txt")
        # Prueba para encontrar el centro del grafo
        self.assertEqual(grafo_logistica.centro_del_grafo(), "Lima")

    # Otros métodos de prueba...

if __name__ == '__main__':
    unittest.main()
