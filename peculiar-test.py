import unittest

from peculiar import (es_par, misma_paridad, alterna_paridad, es_peculiar,
n_esimo_peculiar, cant_peculiares_entre)

class TestEsPar (unittest.TestCase):
    def test_cero(self):
        self.assertTrue(es_par(0))

    def test_un_dígito(self):
        self.assertFalse(es_par(1))
        self.assertTrue(es_par(8))

    def test_muchos_dígitos(self):
        self.assertFalse(es_par(16565551))
        self.assertTrue(es_par(165654864))

class TestMismaParidad (unittest.TestCase):
    def test_verdadero_un_dígito(self):
        self.assertTrue(misma_paridad(0,2))
        self.assertTrue(misma_paridad(5,9))

    def test_verdadero_muchos_dígitos(self):
        self.assertTrue(misma_paridad(6546546,8787494))
        self.assertTrue(misma_paridad(6545421,878783))

    def test_falso_muchos_dígitos(self):
        self.assertFalse(misma_paridad(6546548,878749))
        self.assertFalse(misma_paridad(6545421,878782))
    
class TestAlternaParidad (unittest.TestCase):
    def test_verdadero_un_dígito(self):
        self.assertTrue(alterna_paridad(0))
        self.assertTrue(alterna_paridad(8))

    def test_verdadero_muchos_dígitos(self):
        self.assertTrue(alterna_paridad(123450))
        self.assertTrue(alterna_paridad(854329))
        
    def test_falso_muchos_dígitos(self):
        self.assertFalse(alterna_paridad(123455))
        self.assertFalse(alterna_paridad(7456128))
        
class TestEsPeculiar (unittest.TestCase):
    def test_falso_multiplos_de_22(self):
        self.assertFalse(es_peculiar(88))
        self.assertFalse(es_peculiar(176))
        
    def test_falso_alternan_paridad(self):
        self.assertFalse(es_peculiar(123))
        self.assertFalse(es_peculiar(789))
    
    def test_caso_cero(self):
        self.assertTrue(es_peculiar(0))
        
    def test_verdadero(self):
        self.assertTrue(es_peculiar(1078))
        self.assertTrue(es_peculiar(418))
        
    def test_falso_niguna_condición(self):
        self.assertFalse(es_peculiar(99))
        self.assertFalse(es_peculiar(56442))
        
class TestN_esimoPeculiar (unittest.TestCase):
    def test_n_esimas_posiciones_impares(self):
        self.assertEqual(n_esimo_peculiar(1), 418)
        self.assertEqual(n_esimo_peculiar(15), 1298)

    def test_n_esimas_posiciones_pares(self):
        self.assertEqual(n_esimo_peculiar(2), 616)
        self.assertEqual(n_esimo_peculiar(40), 3696)
        
    def test_caso_cero(self):
        self.assertEqual(n_esimo_peculiar(0), 0)

class TestCantidadDePeculiaresEntre (unittest.TestCase):
    def test_sin_peculiares(self):
        self.assertEqual(cant_peculiares_entre(100, 200), 0)
        self.assertEqual(cant_peculiares_entre(200, 300), 0)
        self.assertEqual(cant_peculiares_entre(900, 1000), 0)
        
    def test_con_peculiares(self):
        self.assertEqual(cant_peculiares_entre(0, 2000), 25)
        self.assertEqual(cant_peculiares_entre(400, 450), 1)

unittest.main() 
