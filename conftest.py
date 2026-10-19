import pytest
from burger import Burger
from bun import Bun

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
   return Bun(name = "Краторная булка №-200i", price = 1255)
