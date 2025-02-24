from odoo import models, fields

class Ingredient(models.Model):
    _name = 'jmm_gestion_restaurantes.ingredient'
    _description = 'Ingredient'

    name = fields.Char(string='Ingredient Name', required=True)
    description = fields.Text(string='Description')
    # Relacion para comprobar la categoria de los ingredientes
    category_id = fields.Many2one(
        'jmm_gestion_restaurantes.category', 
        string='Category'
    )
    # Campo seleccionable
    unit_of_measure = fields.Selection([
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('unit', 'Unit')
    ], string='Unit of Measure')
    stock = fields.Float(string='Current Stock')
    minimum_stock = fields.Float(string='Minimum Stock')
    supplier = fields.Char(string='Main Supplier')
    # Relacion para ver los platos que contienen ese ingrediente
    dish_id = fields.Many2many(
        'jmm_gestion_restaurantes.dish',
        relation="jmm_gestion_ingredient_dish",
        string='Dishes'
    )