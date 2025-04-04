import unittest
from code import ajouter

class TestAjouter(unittest.TestCase):
    def test_ajouter(self):
        # Test de la fonction ajouter avec des messages en cas de succès ou d'échec
        result = ajouter(2, 3)
        self.assertEqual(result, 5, f"Test échoué pour 2 + 3 : {result} attendu 5")
        
        result = ajouter(-1, 1)
        self.assertEqual(result, 0, f"Test échoué pour -1 + 1 : {result} attendu 0")
        
        result = ajouter(0, 0)
        self.assertEqual(result, 0, f"Test échoué pour 0 + 0 : {result} attendu 0")

    def test_succes(self):
        # Exemple de message de succès : ici, vous ne testez pas mais vous imprimez une information.
        print("Tous les tests sont réussis avec succès.")

if __name__ == '__main__':
    unittest.main(verbosity=2)

