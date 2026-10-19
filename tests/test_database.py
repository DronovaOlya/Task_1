from database import Database


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        result = db.available_buns()
        buns = [b.get_name() for b in result]

        assert isinstance(result, list)
        assert len(result) == 3
        assert "black bun" in buns
        assert "white bun" in buns
        assert "red bun" in buns

    def test_available_ingredients(self):
        db = Database()
        result = db.available_ingredients()
        ingredients = [b.get_name() for b in result]

        assert isinstance(result, list)
        assert len(result) == 6
        assert "hot sauce" in ingredients
        assert "sour cream" in ingredients
        assert "chili sauce" in ingredients
        assert "cutlet" in ingredients
        assert "dinosaur" in ingredients
        assert "sausage" in ingredients