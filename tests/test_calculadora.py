import pytest
from src.calculadora import sumar, restar, dividir

def test_sumar():
    assert sumar(3, 2) == 5

def test_restar():
    assert restar(10, 4) == 6

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)