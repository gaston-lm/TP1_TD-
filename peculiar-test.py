import unittest

from peculiar import es_par, misma_paridad

class TestEsPar ( unittest . TestCase ) :
    def test_cero(self):
        self.assertTrue(es_par(0))

    def test_1_dígito(self):
        self.assertFalse(es_par(1))
        self.assertTrue(es_par(8))

    def test_muchos_dígitos(self):
        self.assertFalse(es_par(16565551))
        self.assertTrue(es_par(165654864))

class TestMismaParidad ( unittest . TestCase ) :
    def test_verdadero_1_dígito(self):
        self.assertTrue(misma_paridad(0,2))
        self.assertTrue(misma_paridad(5,9))

    def test_verdadero_muchos_dígitos(self):
        self.assertTrue(misma_paridad(6546546,8787494))
        self.assertTrue(misma_paridad(6545421,878783))

    def test_falso_muchos_dígitos(self):
        self.assertFalse(misma_paridad(6546548,878749))
        self.assertFalse(misma_paridad(6545421,878782))
        
unittest.main() 
