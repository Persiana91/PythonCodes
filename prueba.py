import unittest
import cambiar_texto


class ProbarCambiarTexto(unittest.TestCase):

    def test_mayusculas(self):

        palabra = "hola"
        resultado = cambiar_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "HOLA")


if __name__ == '__main__':
    unittest.main()
