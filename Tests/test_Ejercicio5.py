import pytest
from Ejercicio5 import clasificar_numero



# PRUEBAS DE NÚMEROS PARES

def test_par_no_multiplo_5():
    assert clasificar_numero(2) == "Es par"

def test_par_multiplo_5():
    assert clasificar_numero(10) == "Es par y múltiplo de 5"



# PRUEBAS DE NÚMEROS IMPARES

def test_impar_no_multiplo_5():
    assert clasificar_numero(3) == "Es impar"

def test_impar_multiplo_5():
    assert clasificar_numero(15) == "Es impar y múltiplo de 5"



# PRUEBAS DE CASOS EXTREMOS

def test_cero():
    # 0 es par y múltiplo de 5
    assert clasificar_numero(0) == "Es par y múltiplo de 5"