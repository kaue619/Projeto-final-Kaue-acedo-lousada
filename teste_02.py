import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_simples(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()
