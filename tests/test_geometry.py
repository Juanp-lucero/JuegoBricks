# tests/test_geometry.py

import pytest
from src.geometry import area_circulo, area_rectangulo, area_triangulo

def test_area_circulo():
    assert round(area_circulo(1), 2) == 3.14
    assert round(area_circulo(5), 2) == 78.54
    assert round(area_circulo(10), 2) == 314.16

def test_area_rectangulo():
    assert area_rectangulo(4, 5) == 20
    assert area_rectangulo(10, 2) == 20
    assert area_rectangulo(6, 3) == 18

def test_area_triangulo():
    assert area_triangulo(4, 5) == 10
    assert area_triangulo(10, 2) == 10
    assert area_triangulo(6, 3) == 9
