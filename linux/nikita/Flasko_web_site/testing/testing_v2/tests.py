import unittest
import main # тестируемый модуль

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.test_int(-2), 4)
                
    def test_string(self):
        try:
            main.test_int("nikita")
        except TypeError:
            return True
        raise TypeError   

    def test_nikita(self):
        try:
            main.test_int(3)
        except TypeError:
            return True
        raise TypeError