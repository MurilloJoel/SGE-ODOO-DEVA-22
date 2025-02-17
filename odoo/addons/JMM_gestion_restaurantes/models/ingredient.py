from odoo import models, fields

class Ingredient(models.Model):
    _name = 'JMM_kitchen.ingredient'
    _description = 'Ingredient'

    name = fields.Char(string='Ingredient Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one(
        'JMM_kitchen.category', 
        string='Category'
    )
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