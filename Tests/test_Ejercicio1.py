# Supongamos que tienes un archivo `calculadora.py` con una función `sumar`:

# calculadora.py
def sumar(a, b):
    return a + b

# Tu archivo de prueba `tests/test_calculadora.py` se vería así:

# tests/test_calculadora.py
from calculadora import sumar

def test_sumar_dos_numeros_enteros():
    assert sumar(2, 3) == 5

def test_sumar_con_cero():
    assert sumar(5, 0) == 5