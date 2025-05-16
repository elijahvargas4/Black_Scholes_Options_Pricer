import pytest
from black_scholes import black_scholes_call, black_scholes_put

def test_black_scholes_call():
    # Example values
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    price = black_scholes_call(S, K, T, r, sigma)
    assert price > 0

def test_black_scholes_put():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    price = black_scholes_put(S, K, T, r, sigma)
    assert price > 0