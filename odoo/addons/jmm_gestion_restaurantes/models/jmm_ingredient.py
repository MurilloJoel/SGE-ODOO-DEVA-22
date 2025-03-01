from odoo import models, fields, api, exceptions

class Ingredient(models.Model):
    _name = 'jmm_gestion_restaurantes.ingredient'
    _description = 'Ingredient'
    
    name = fields.Char(string='Ingredient Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one(
        'jmm_gestion_restaurantes.category', 
        string='Category',
        required=True
    )
    unit_of_measure = fields.Selection([
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('unit', 'Unit')
    ], string='Unit of Measure', required=True)
    stock = fields.Float(string='Current Stock')
    minimum_stock = fields.Float(string='Minimum Stock')
    supplier = fields.Char(string='Main Supplier')
    dish_id = fields.Many2many(
        'jmm_gestion_restaurantes.dish',
        relation="jmm_gestion_ingredient_dish",
        string='Dishes'
    )
    image = fields.Binary(string='Ingredient Image', help='Seleccionar Imagen')

    _sql_constraints = [
        ('unique_ingredient_name', 'UNIQUE(name)', '¡Nombre del ingrediente debe ser único!'),
        ('positive_stock', 'CHECK(stock >= 0)', '¡Stock no puede ser negativo!'),
        ('minimum_stock_check', 'CHECK(minimum_stock >= 0)', '¡Stock mínimo ≥ 0!'),
        ('stock_above_minimum', 'CHECK(stock >= minimum_stock)', '¡Stock actual ≥ mínimo!')
    ]

    @api.constrains('unit_of_measure')
    def _check_unit_of_measure(self):
        valid_units = ['kg', 'g', 'l', 'ml', 'unit']
        if self.unit_of_measure not in valid_units:
            raise exceptions.ValidationError('¡Unidad de medida no válida!')