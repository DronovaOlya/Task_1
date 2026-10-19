from ingredient import Ingredient
import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize('price,name,ingredient_type', [
    (300, "Хрустящие минеральные кольца", INGREDIENT_TYPE_FILLING),
    (874, "Плоды Фалленианского дерева", INGREDIENT_TYPE_FILLING),
    (88, "Соус с шипами Антарианского плоскоходца", INGREDIENT_TYPE_SAUCE),
    (90, "Соус Spicy-X", INGREDIENT_TYPE_SAUCE)
])
    def test_get_price(self, price, name, ingredient_type):
        ingredient = Ingredient(price=price, name=name, ingredient_type=ingredient_type)

        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type