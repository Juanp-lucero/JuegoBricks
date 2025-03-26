# tests/test_prime.py

import pytest
from src.prime import is_prime

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(13) is True
    assert is_prime(4) is False
    assert is_prime(100) is False
    assert is_prime(29) is True
