import unittest
from code import ajouter

class TestAjouter(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(ajouter(2, 3), 5)
        self.assertEqual(ajouter(-1, 1), 0)
        self.assertEqual(ajouter(0, 0), 0)
        self.assertEqual(ajouter(100, 250), 350)

if __name__ == "__main__":
    unittest.main()
