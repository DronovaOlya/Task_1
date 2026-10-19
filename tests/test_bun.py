from bun import Bun
import pytest

class TestBun:

    @pytest.mark.parametrize('name,price', [
    ("Краторная булка №-200i", 1255),
    ("Флюоресцентная булка R2-D3", 988)
])
    def test_bun_name_and_price(self, name, price):
        bun = Bun(name=name, price=price)

        assert bun.get_name() == name
        assert bun.get_price() == price