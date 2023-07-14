import unittest
import LibreriaUnittest

class Test(unittest.TestCase):
    def test_mayuscula(self):
        palabra="Prueba de libreria"
        result = LibreriaUnittest.todo_mayusculas(palabra)
        self.assertEqual(result, "PRUEBA DE LIBRERIA")
        print (result)
if __name__ == "__main__":
    unittest.main()
