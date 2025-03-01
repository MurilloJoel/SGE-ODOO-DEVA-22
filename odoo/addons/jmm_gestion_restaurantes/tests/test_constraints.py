from odoo.tests import TransactionCase

class TestConstraints(TransactionCase):
    def setUp(self):
        super(TestConstraints, self).setUp()
        self.Category = self.env['jmm_gestion_restaurantes.category']
        self.Dish = self.env['jmm_gestion_restaurantes.dish']
        self.Ingredient = self.env['jmm_gestion_restaurantes.ingredient']
        self.Preparation = self.env['jmm_gestion_restaurantes.preparation']

    def test_category_unique_name(self):
        self.Category.create({'name': 'Test Cat'})
        with self.assertRaises(Exception):
            self.Category.create({'name': 'Test Cat'})

    def test_dish_price_validation(self):
        with self.assertRaises(Exception):
            self.Dish.create({'name': 'Test Dish', 'price': -10})

    def test_ingredient_stock_validation(self):
        cat = self.Category.create({'name': 'Test Cat'})
        with self.assertRaises(Exception):
            self.Ingredient.create({
                'name': 'Test Ing',
                'category_id': cat.id,
                'stock': -5,
                'unit_of_measure': 'kg'
            })

    def test_preparation_time_validation(self):
        with self.assertRaises(Exception):
            self.Preparation.create({
                'name': 'Test Prep',
                'time': -5,
                'equipment': 'Test'
            })

    def test_ingredient_unit_validation(self):
        cat = self.Category.create({'name': 'Test Cat'})
        with self.assertRaises(Exception):
            self.Ingredient.create({
                'name': 'Test Ing',
                'category_id': cat.id,
                'unit_of_measure': 'invalid',
                'stock': 10
            })