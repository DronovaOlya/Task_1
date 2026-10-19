from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from ingredient_name import name_ingredient_sause, name_ingredient_filling

class TestBurger:
    
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient(self, burger):
        burger.add_ingredient(ingredient = name_ingredient_sause)

        assert name_ingredient_sause in burger.ingredients

    def test_remove_ingredient(self, burger):
        burger.add_ingredient(ingredient = name_ingredient_sause)
        index = burger.ingredients.index(name_ingredient_sause)
        burger.remove_ingredient(index = index)

        assert name_ingredient_sause not in burger.ingredients

    def test_move_ingredient(self, burger):
        burger.add_ingredient(ingredient = name_ingredient_sause)
        index = burger.ingredients.index(name_ingredient_sause)
        burger.add_ingredient(ingredient = name_ingredient_filling)
        new_index = 1
        burger.move_ingredient(index = index, new_index = new_index)
        
        assert burger.ingredients.index(name_ingredient_sause) == new_index

    def test_get_price(self, burger, bun):
        name_ingredient = Ingredient(ingredient_type = INGREDIENT_TYPE_SAUCE, name = "Соус фирменный Space Sause", price = 80)
        name_ingredient_1 = Ingredient(ingredient_type = INGREDIENT_TYPE_FILLING, name = "Хрустящие минеральные кольца", price = 300)

        burger.set_buns(bun)   
        burger.add_ingredient(ingredient = name_ingredient)
        burger.add_ingredient(ingredient = name_ingredient_1)

        cost = bun.get_price() * 2 + name_ingredient.get_price() + name_ingredient_1.get_price()
        
        price = burger.get_price()

        assert price == cost

    def test_get_receipt(self, burger, bun):
        name_ingredient = Ingredient(ingredient_type = INGREDIENT_TYPE_SAUCE, name = "Соус фирменный Space Sause", price = 80)
        name_ingredient_1 = Ingredient(ingredient_type = INGREDIENT_TYPE_FILLING, name = "Хрустящие минеральные кольца", price = 300)

        burger.set_buns(bun)   
        burger.add_ingredient(ingredient = name_ingredient)
        burger.add_ingredient(ingredient = name_ingredient_1)

        receipt = burger.get_receipt()
        bun_name = bun.get_name()
        price = str (burger.get_price())

        assert bun_name in receipt
        assert price in receipt